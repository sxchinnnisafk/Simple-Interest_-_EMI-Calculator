# Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY finance_utils.py test_finance_utils.py ./

RUN pip install --no-cache-dir pytest

CMD ["sh", "-c", "pytest -v && python finance_utils.py"]
