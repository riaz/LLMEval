# app/Dockerfile

FROM python:3.11-bullseye

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/riaz/LLMEval.git

RUN cd LLMEval/frontend

COPY setup.sh setup.sh
COPY requirements.txt requirements.txt

RUN chmod u+x setup.sh

RUN ./setup.sh

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

#ENTRYPOINT ["streamlit", "run", "app/main.py", "--server.port=8501", "--server.address=0.0.0.0"]






