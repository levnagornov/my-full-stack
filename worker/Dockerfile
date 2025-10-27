FROM ubuntu:24.04

# Установка зависимостей
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 python3-pip python3-venv \
    build-essential curl redis-tools \
    && apt-get clean && rm -rf /var/lib/apt/lists/*
    
WORKDIR /app

COPY requirements.txt .

# Создаем виртуальное окружение
RUN python3 -m venv /opt/venv \
    && /opt/venv/bin/pip install --upgrade pip \
    && /opt/venv/bin/pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1
ENV PATH="/opt/venv/bin:$PATH"

CMD ["celery", "-A", "worker.celery_app", "worker", "--loglevel=info", "--concurrency=2"]



