import os
import threading

from sqlalchemy import create_engine
from sqlalchemy.sql import text

class PostgresMasterScheduler(threading.Thread):
    
    def __init__(self, input_queue, **kwargs):
        super().__init__(**kwargs)
        self._input_queue = input_queue
        self.start()

    def run(self):
        while True:

            val = self._input_queue.get()
            if val == "DONE":
                break

            symbol, price, timestamp = val

            postgres_worker = PostgresWorker(symbol, price, timestamp)
            postgres_worker.insert_into_db()


class PostgresWorker:

    def __init__(self, symbol, price, timestamp):
        self._symbol = symbol
        self._price = price
        self._timestamp = timestamp

        self._PG_USER = os.getenv('DB_USER')
        self._PG_PASSWD = os.getenv('DB_PASSWD')
        self._PG_HOST = os.getenv('DB_HOST')
        self._PG_NAME = os.getenv('DB_NAME')

        self._engine = create_engine(f"postgresql://{self._PG_NAME}:{self._PG_PASSWD}@{self._PG_HOST}/{self._PG_NAME}")
    
    def _create_insert_query(self):
        raw_sql = """INSERT INTO prices (symbol, price, insert_time_dt) VALUES (:symbol, :price, :timestamp)"""

        return raw_sql

    def insert_into_db(self):
        insert_query = self._create_insert_query()

        with self._engine.connect() as conn:
            conn.execute(text(insert_query), {'symbol': self._symbol, 'price': self._price, 'timestamp': self._timestamp})
