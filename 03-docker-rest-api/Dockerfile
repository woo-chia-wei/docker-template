FROM python:3.7.3-slim

WORKDIR /project
COPY . /project

RUN pip install Flask
RUN pip install flask-cors

EXPOSE 5000

CMD ["python","app.py"]
