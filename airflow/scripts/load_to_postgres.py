import pandas as pd
from utils.postgres_helper import get_connection
from config import LOCAL_PATHS
from utils.logger import get_logger

logger = get_logger(__name__)

def load_to_postgres():
    conn = get_connection()
    cursor = conn.cursor()

    df = pd.read_csv(LOCAL_PATHS["transformed_data"])
    logger.info(f"Inserting {len(df)} records into PostgreSQL...")

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INT PRIMARY KEY,
            title TEXT,
            price FLOAT,
            category TEXT
        )
    ''')
    insert_query = '''
        INSERT INTO products (id, title, price, category)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (id) DO NOTHING
    '''
    for _, row in df.iterrows():
        cursor.execute(insert_query, (row['id'], row['title'], row['price'], row['category']))

    conn.commit()
    cursor.close()
    conn.close()
    logger.info("✅ Data successfully loaded into PostgreSQL.")

if __name__ == "__main__":
    load_to_postgres()
