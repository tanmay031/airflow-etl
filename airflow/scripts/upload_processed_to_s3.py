from utils.s3_helper import upload_to_s3
from config import LOCAL_PATHS

def upload_processed_to_s3():
    """
    Upload the transformed data file to S3.
    """
    upload_to_s3(LOCAL_PATHS["transformed_data"], "processed/transformed_data.csv")

if __name__ == "__main__":
    upload_processed_to_s3()
