import os

# PostgreSQL
POSTGRES = {
    "host": os.getenv("POSTGRES_HOST", "postgres"),
    "port": os.getenv("POSTGRES_PORT", "5432"),
    "db": os.getenv("POSTGRES_DB", "airflow"),
    "user": os.getenv("POSTGRES_USER", "airflow"),
    "password": os.getenv("POSTGRES_PASSWORD", "airflow")
}

# AWS
AWS = {
    "access_key": os.getenv("AWS_ACCESS_KEY_ID"),
    "secret_key": os.getenv("AWS_SECRET_ACCESS_KEY"),
    "region": os.getenv("AWS_DEFAULT_REGION", "eu-north-1"),
    "bucket_name": os.getenv("S3_BUCKET_NAME", "etl-datalake-portfolio")
}

# File Paths
LOCAL_PATHS = {
    "raw_data": "/opt/airflow/tmp/raw_data.json",
    "transformed_data": "/opt/airflow/tmp/transformed_data.csv"
}
