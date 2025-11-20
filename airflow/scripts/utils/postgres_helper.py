import psycopg2
from psycopg2.extras import RealDictCursor
from config import POSTGRES
from utils.logger import get_logger

logger = get_logger(__name__)

def get_connection():
    return psycopg2.connect(
        host=POSTGRES["host"],
        port=POSTGRES["port"],
        database=POSTGRES["db"],
        user=POSTGRES["user"],
        password=POSTGRES["password"]
    )
