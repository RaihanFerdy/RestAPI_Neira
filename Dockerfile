# python version
FROM python:3.8-slim

# working directory
WORKDIR /app

# copy requirements to working directory
COPY requirements.txt /app/

# install requirements
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# copy all file to working directory
COPY . /app/

# setting environment flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development

# command running flask
CMD ["flask", "run"]