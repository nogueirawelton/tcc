FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app

RUN pip3 install --no-cache-dir --break-system-packages -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:server", "--host", "0.0.0.0", "--port", "8000", "--reload"]
