FROM python:3.7.3-slim

WORKDIR /project
COPY . /project

RUN pip install pandas jupyter

EXPOSE 8888

CMD ["jupyter","notebook","--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
