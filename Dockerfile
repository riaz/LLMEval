FROM python:3.8-bullseye
WORKDIR /code
COPY requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
#CMD ["fastapi", "run", "app/main.py", "--port", "5000"] - for fast api
CMD ["python", "-m","streamlit", "run", "app/main.py", "--server.port", "5000"] 