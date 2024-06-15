<h1 align="center"> RestAPI Neira Sphere </h1>
<p align="center"> Neira Sphere AI Model API Documentation </p>
<div align="center">
<img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
<img src="https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white">
<img src="https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white">
<img src="https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white">
<img src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white">
</div>


# Teams
- [Zona Diatri](https://www.linkedin.com/in/zona-diatri-1275a0222/) (Design Researcher) 
- [Baren Baruna Harahap](https://www.linkedin.com/in/barenbarunaharahap/) (Data Engineer)
- [Muhammad Iqmal Basori](https://www.linkedin.com/in/muhammad-iqmal-basori-b6017128a/) (Machine Learning Engineer)
- [Muhammad Raihan Ferdyansyah](https://www.linkedin.com/in/muhammad-raihan-ferdyansyah/) (Machine Learning Ops)


# Requirements
- Devices with Windows 10/11 64-bit system
- Minimum 4GB RAM
- Minimum 40-80GB remaining storage
- Download & Install [Postman Apps](https://www.postman.com/downloads/)
- Download & Install [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- Download & Install [Python 3.8+](https://www.python.org/downloads/)


# Steps
## A. Setup and Installation
1. Clone the repository
```
git clone https://github.com/RaihanFerdy/RestAPI_Neira.git
```
2. Navigate to the project directory
```
cd RestAPI_Neira
```
3. Create and activate a virtual environment (optional but recommended)
```
python -m venv venv
venv\Scripts\activate
```
4. Install the required dependencies
```
pip install -r requirements.txt
```
5. Add your [API Groq](https://console.groq.com/keys) and [API IBM Cloud](https://cloud.ibm.com/iam/apikeys) to the `.env` file
```
API_GROQ=YOUR_TOKEN_GROQ
API_IBM=YOUR_TOKEN_IBM
```

## B. Usage
### Running in terminal
1. Run in terminal `python -m flask run` or `python app.py`
2. The API will be accessible at `http://127.0.0.1:5000`

### Running in Docker Desktop
1. Open Docker Desktop
2. Open terminal and build the Docker Image
```
docker build -t restapi_neira .
```
3. Run the Docker Container
```
docker run -d -p 5000:5000 --name restapi_neira_container restapi_neira
```
4. Verify the container is running
```
docker ps
```

### API Testing with Postman
1. Open Postman, then add a new session in your workspace.
   ![](https://i.imgur.com/gDbWIW1.png)
2. Change the method to POST and enter `http://127.0.0.1:5000` appending `/result` to the end of the URL.
   ![](https://i.imgur.com/ClL1StD.png)
3. Select the `Body` tab and choose `form-data`. Change the `key` type from `text` to `file` for the file you want to upload.
   ![](https://i.imgur.com/9ykMx3E.png)
   ![](https://i.imgur.com/BZI6fIh.png)
4. Send the request and view the response from the API.
   ![](https://i.imgur.com/xprYr4U.png)
5. Send the request to Deployment API `https://neira-api.1hs5xuud6atv.us-south.codeengine.appdomain.cloud` and appending `/result` to the end of the URL
   ![](https://i.imgur.com/7YZjoXW.png)
---
