# app/Dockerfile

FROM python:3.11-bullseye

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/riaz/LLMEval.git .

RUN cd LLMEval/frontend

CMD setup.sh

EXPOSE 8501



