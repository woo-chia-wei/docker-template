FROM python:3.7.3-slim

WORKDIR /project
COPY . /project

RUN pip install tqdm

ENTRYPOINT ["python", "calculate_primes.py"]