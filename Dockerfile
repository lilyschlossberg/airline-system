FROM python:3.9-slim
ENV DOCKER_CONFIG=/root/.docker/

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
