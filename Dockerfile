FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Копируем зависимости
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . .

# Создаём папку для базы (если нужно)
RUN mkdir -p /app/data

CMD ["python", "bot.py"]
