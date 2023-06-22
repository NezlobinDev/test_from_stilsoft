FROM --platform=linux/amd64 python:3.10.10-slim

ENV PYTHONDONTWRITEBYCODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir

RUN apt-get update && apt-get upgrade -y \
    && apt-get install --no-install-recommends -y \
    bash \
    curl \
    wait-for-it


COPY docker-entrypoint.sh /

RUN chmod +x /docker-entrypoint.sh
COPY . /app
ENTRYPOINT ["/docker-entrypoint.sh"]