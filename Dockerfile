FROM python:3.12-alpine

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY app/ .

RUN adduser -D appuser

USER appuser

EXPOSE 8000

CMD ["python", "main.py"]
