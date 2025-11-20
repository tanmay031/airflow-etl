from utils.s3_helper import upload_to_s3
from config import LOCAL_PATHS

def upload_raw_to_s3():
    """
    Upload the raw data file to S3.
    """
    upload_to_s3(LOCAL_PATHS["raw_data"], "raw/raw_data.json")

if __name__ == "__main__":
    upload_raw_to_s3()
