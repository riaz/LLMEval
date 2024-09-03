# LLMEval
Evaluating LLM Pipelines

# Local Setup - api

    conda create -n pyswe python=3.11
    conda activate pyswe
    pip install -r requirements.txt
    fastapi run app.py

    # check localhost:8000 on postman or a browser

# Local setup helm

    conda create -n helm python=3.8
    conda activate helm
    pip install crfm-helm

    # docker run -d -p 7777:7777 -it llmeval-web /bin/bash

    docker run -d -p 7777:7777 -it llmeval-web /bin/bash

    docker run --rm -i -t --net=host llmeval-web /bin/bash

    http://localhost:8080/login/?next=http%3A%2F%2Flocalhost%3A8080%2Fhome

# Todo:

    1. Create a streamlit app that uses the airflow api to display dags and their runs
    2. making it possible to run helm on the docker
    3. trying to create a new dag 
    4. steamlit app to display airflow components in ui
    5. streamlit app using an api call that runs a server with connectio