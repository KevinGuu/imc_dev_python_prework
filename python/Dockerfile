FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY bank.py main.py .

CMD ["python3", "main.py"]


# docker run --rm -itt --network imc bank