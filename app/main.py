#create a streamlit application that had 2 panels. The left panels has two links where the first one is selected and refers to the latest airflow pipeline run and the 2nd button is for all airflow pipeline runs historically.  We want the right panel to display airflow runs as a api call with dag id as the parameter. 

import streamlit as st
import requests

dag_id = "riaz_tutorial_dag"

# Streamlit app
st.title('Airflow Pipeline Runs')

limit = None

def fetch_dag_runs(dag_id=None, limit=None):
    # Replace with your actual Airflow API endpoint
    api_url = f"http://localhost:8080/api/v1/dags/{dag_id}/dagRuns" if dag_id else "http://localhost:8080/api/v1/dags/~/dagRuns"
    response = requests.get(api_url, auth=('airflow', 'airflow'))
    response_json = response.json()
    if limit:
        return response_json['dag_runs'][:limit]
    else:
        return response_json
    
def fetch_latest_run():
    return fetch_dag_runs(limit=-1)[0]

def fetch_historical_runs():
    return fetch_dag_runs(limit=10)

# Left panel with links
with st.sidebar:

    if st.button('Latest Run'):
        # Fetch and display the latest run
        #latest_run = fetch_latest_run()
        #st.write(latest_run)
        limit = 1

    if st.button('Historical Runs'):
        # Fetch and display historical runs
        limit = 10
        #historical_runs = fetch_historical_runs()
        #st.write(historical_runs)

# Right panel with DAG runs
st.header('DAG Runs')

#if limit:
#    # Fetch and display DAG runs
#    dag_runs = fetch_dag_runs(limit=limit)
#    st.write(dag_runs)

