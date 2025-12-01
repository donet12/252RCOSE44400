FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir Flask==3.1.2 requests==2.32.5

COPY app.py .
COPY templates/ templates/

EXPOSE 5000

CMD ["python", "app.py"]

