FROM python:3.9.16-slim

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app/

EXPOSE 8080

CMD ["python", "./api/main.py"]


# pip list --format=freeze > requirements.txt
# docker build -t the-mle-challenge .
# docker run -p 8080:8080 the-mle-challenge