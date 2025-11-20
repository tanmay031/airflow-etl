import requests
import json
import os
from config import LOCAL_PATHS
from utils.logger import get_logger

logger = get_logger(__name__)

def fetch_data():
    url = "https://fakestoreapi.com/products"
    response = requests.get(url)
    data = response.json()

    os.makedirs(os.path.dirname(LOCAL_PATHS["raw_data"]), exist_ok=True)
    with open(LOCAL_PATHS["raw_data"], 'w') as f:
        json.dump(data, f)
    logger.info("Raw data fetched and saved locally.")

if __name__ == "__main__":
    fetch_data()
