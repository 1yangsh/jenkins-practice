FROM python:3.7.9-stretch

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

EXPOSE 80

CMD ["python","app.py"]