FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --only-binary :all: -r requirements.txt

COPY calculadora.py .
COPY test_calculadora.py .

CMD ["pytest", "-v"]