from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
import os

# Add scripts path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../scripts')))

from fetch_data import fetch_data
from upload_raw_to_s3 import upload_raw_to_s3
from transform_data import transform_data
from upload_processed_to_s3 import upload_processed_to_s3
from load_to_postgres import load_to_postgres

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'product_trend_dag',
    default_args=default_args,
    description='ETL pipeline for product trends with Data Lake and Data Warehouse',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2025, 1, 1),
    catchup=False,
) as dag:

    # 1️ Fetch raw data from external API
    task_fetch = PythonOperator(
        task_id='fetch_data',
        python_callable=fetch_data
    )

    # 2️ Store raw, unprocessed data in S3 → Data Lake (RAW LAYER)
    task_upload_raw_s3 = PythonOperator(
        task_id='upload_raw_to_s3',
        python_callable=upload_raw_to_s3
    )

    # 3️ Read raw data from Data Lake and transform it
    task_transform = PythonOperator(
        task_id='transform_data',
        python_callable=transform_data
    )

    # 4️ Store transformed/structured dataset in S3
    #    → Data Lake (PROCESSED / CURATED LAYER)
    task_upload_processed_s3 = PythonOperator(
        task_id='upload_processed_to_s3',
        python_callable=upload_processed_to_s3
    )

    # 5️ Load analytical-friendly data into Postgres
    #    → Data Warehouse (structured, optimized for queries)
    task_load_postgres = PythonOperator(
        task_id='load_to_postgres',
        python_callable=load_to_postgres
    )

    # Workflow definition:
    task_fetch >> task_upload_raw_s3 >> task_transform
    task_transform >> [task_upload_processed_s3, task_load_postgres]

