# استخدم بيئة Python مخصصة لنشر النموذج على Replicate
FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir pillow torch torchvision

CMD ["python", "-m", "replicate"]
