from datetime import datetime
import requests
from airflow import DAG
from airflow.operators.python import PythonOperator


def trigger_pipeline():
    response = requests.post("http://api:8000/pipeline/trigger?limit=10", timeout=30)
    response.raise_for_status()
    return response.json()


with DAG(
    dag_id="pipeline_monitoring_dag",
    start_date=datetime(2025, 1, 1),
    schedule="@hourly",
    catchup=False,
    tags=["pipeline", "monitoring"],
) as dag:
    PythonOperator(
        task_id="trigger_pipeline_via_api",
        python_callable=trigger_pipeline,
    )
