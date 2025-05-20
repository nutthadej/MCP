FROM python:3.11-slim

WORKDIR /app

# 🔧 ติดตั้ง git เพื่อใช้ติดตั้ง requirements จาก GitHub
RUN apt-get update && \
    apt-get install -y git && \
    apt-get clean

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "server.py"]
