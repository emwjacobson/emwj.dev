FROM python:3.8

WORKDIR /app

ENV PATH="/scripts:${PATH}"

RUN apt-get update && apt-get install -y --no-install-recommends \
    default-libmysqlclient-dev \
    build-essential \
    wget && \
    rm -rf /var/lib/apt/lists/*

COPY scripts /scripts
RUN chmod +x /scripts/*

COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt

COPY app app
COPY portfolio portfolio
COPY manage.py .

RUN useradd user
RUN mkdir -p /app/static
RUN chown -R user:user /app
USER user

CMD ["entrypoint.sh"]
