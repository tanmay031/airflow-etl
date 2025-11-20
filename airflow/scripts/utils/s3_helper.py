import boto3
from botocore.exceptions import ClientError
from config import AWS
from utils.logger import get_logger

logger = get_logger(__name__)

def upload_to_s3(local_path, s3_key):
    try:
        s3 = boto3.client(
            "s3",
            aws_access_key_id=AWS["access_key"],
            aws_secret_access_key=AWS["secret_key"],
            region_name=AWS["region"]
        )
        logger.info(f"Uploading {local_path} → s3://{AWS['bucket_name']}/{s3_key}")
        s3.upload_file(local_path, AWS["bucket_name"], s3_key)
        logger.info("File uploaded successfully.")
    except ClientError:
        logger.error("S3 upload failed.", exc_info=True)
