from keras.applications.vgg19 import preprocess_input # type: ignore
import numpy as np
from PIL import Image
from flask import Flask, request, jsonify
from flask_cors import CORS
from groq import Groq
import time, dotenv, os, requests

app = Flask(__name__)
CORS(app)
dotenv.load_dotenv()

@app.route('/')
def index():
    return "<h1>Neira Sphere</h1>"

@app.route('/result', methods=['POST'])
def upload():
    waktu_awal = time.time()
    if request.method == 'POST':
        # request image from user and save to local
        file = request.files['file']
        file.save(f"./img_raw/{file.filename}")
        
        # define class categories
        output_class = ["battery", "glass", "metal", "organic", "paper", "plastic"]
        
        # import API from IBM Cloud
        api_ibm = os.getenv("API_IBM")
        token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": api_ibm, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
        mltoken = token_response.json()["access_token"]
        
        # preprocess image
        def preprocessing_input(img_path):
            img = Image.open(img_path)
            img = img.resize((224, 224))
            img = np.array(img)
            img = np.expand_dims(img, axis=0)
            img = preprocess_input(img)
            return img
        
        # use groq AI to generate descriptions
        def ai_description(category):
            dotenv.load_dotenv()
            token = os.getenv("API_GROQ")
            client = Groq(api_key=token)
            model = "llama3-70b-8192"
            messages = [
                {"role": "system", "content": """Anda adalah seorang propagandis perlindungan lingkungan. Tugas Anda adalah memberi saya informasi paling penting
                                                 tentang jenis sampah yang saya berikan dalam daftar hanya 2 baris, dengan fokus pada proses penguraian dan cara mengatasinya.
                                                 Hindari detail atau penjelasan yang tidak perlu, dan jawab langsung tanpa menggunakan
                                                 nama jenis sampah, styling, atau pemformatan khusus lainnya jawab menggunakan bahasa indonesia"""},
                {"role": "user", "content": f"{category}"}
            ]
            chat = client.chat.completions.create(model=model, messages=messages)
            reply = chat.choices[0].message.content
            return reply
        
        # prediction image use API from IBM Cloud
        def predict_image(img_path):
            try:
                # Send image to IBM for prediction
                img = preprocessing_input(img_path)
                payload_scoring = {"input_data": [{"values": img.tolist()}]}
                header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}
                scoring_url = "https://us-south.ml.cloud.ibm.com/ml/v4/deployments/restapi/predictions?version=2021-05-01"
                
                # response result from IBM
                response_scoring = requests.post(scoring_url, json=payload_scoring, headers=header)
                result = response_scoring.json()['predictions'][0]['values'][0]
                predicted_class_idx = np.argmax(result)
                predicted_class = output_class[predicted_class_idx]
                predicted_probability = result[predicted_class_idx]
                
                # generate description from groq API
                description = ai_description(predicted_class)
                
                # generate result in JSON format
                result = {
                    "accuracy": f"{predicted_probability:.2%}",
                    "class_category": predicted_class.title(),
                    "description": description
                }
                waktu_akhir = time.time()
                lama_waktu = waktu_akhir - waktu_awal
                print(f"\nLama waktu: {lama_waktu} detik")
                return result
            except:
                result_error = {
                    "accuracy": "-%",
                    "class_category": "Not Found",
                    "description": "Not Found",
                }
                waktu_akhir = time.time()
                lama_waktu = waktu_akhir - waktu_awal
                print(f"\nLama waktu: {lama_waktu} detik")
                return result_error
        
        # return result for user made request
        try:
            return jsonify(predict_image(f"./img_raw/{file.filename}")), os.remove(f"./img_raw/{file.filename}")
        except:
            return "<h1>Error System<h1>"
            
if __name__ == '__main__':
    app.run(debug=True)
