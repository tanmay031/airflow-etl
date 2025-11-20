import json
import pandas as pd
from config import LOCAL_PATHS
from utils.logger import get_logger

logger = get_logger(__name__)

def transform_data():
    with open(LOCAL_PATHS["raw_data"], 'r') as f:
        data = json.load(f)

    df = pd.DataFrame(data)[["id", "title", "price", "category"]]
    df.to_csv(LOCAL_PATHS["transformed_data"], index=False)
    logger.info("Data transformed and saved to CSV.")

if __name__ == "__main__":
    transform_data()
