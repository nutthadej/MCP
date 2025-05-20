FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y git && \
    apt-get clean

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "server.py"]
# force rebuild 2025-05-20
FROM python:3.11-slim
...
