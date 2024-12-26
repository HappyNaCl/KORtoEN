FROM python:3.10-slim

WORKDIR /app

RUN apt update && apt install -y --no-install-recommends \
    gcc \
    python3-dev \
    libstdc++6 \
    libc6-dev \
    libopenblas-dev \
    libfreetype6-dev \
    libpng-dev \
    libjpeg-dev \
    libtiff-dev \
    libharfbuzz-dev \
    libfribidi-dev \
    liblcms2-dev \
    zlib1g-dev \
    libwebp-dev \
    libcairo2-dev \
    libpango1.0-dev \
    libgdk-pixbuf2.0-dev \
    libgl1 \
    tesseract-ocr \
    tesseract-ocr-kor \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install --no-cache-dir --upgrade pip setuptools wheel \
    && pip install --no-cache-dir -r requirement.txt

CMD ["flask", "run", "--host=0.0.0.0"]
