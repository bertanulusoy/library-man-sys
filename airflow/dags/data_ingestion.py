import os
from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator
from ingest_library_data import ingest_data_callable

AIRFLOW_HOME = os.environ.get("AIRFLOW_HOME", "/opt/airflow/")

MONGO_HOST = os.getenv('MONGO_HOST')
MONGO_USER = os.getenv('MONGO_USER')
MONGO_PASSWORD = os.getenv('MONGO_PASSWORD')
MONGO_PORT = os.getenv('MONGO_PORT')
MONGO_DATABASE = os.getenv('MONGO_DATABASE')
DATA_URL = AIRFLOW_HOME + '/library_data/' #+ os.getenv('DATA_FOLDER')
BOOKS_DATA_URL = DATA_URL + 'books.csv'
BORROWERS_DATA_URL = DATA_URL + 'borrowers.csv'
TRANSACTIONS_DATA_URL = DATA_URL + 'transactions.csv'


local_workflow = DAG(
    "localIngestionDAG",
    schedule_interval="0 6 2 * *",
    start_date=datetime(2022, 1, 1)
)
with local_workflow:
    ingest_book = PythonOperator(
        task_id='ingest_book',
        python_callable=ingest_data_callable,
        op_kwargs=dict(
            user=MONGO_USER,
            password=MONGO_PASSWORD,
            host=MONGO_HOST,
            port=MONGO_PORT,
            db=MONGO_DATABASE,
            table_name='Book',
            csv_file_url=BOOKS_DATA_URL
        )
    )

    ingest_borrowers = PythonOperator(
        task_id='ingest_borrowers',
        python_callable=ingest_data_callable,
        op_kwargs=dict(
            user=MONGO_USER,
            password=MONGO_PASSWORD,
            host=MONGO_HOST,
            port=MONGO_PORT,
            db=MONGO_DATABASE,
            table_name='Borrower',
            csv_file_url=BORROWERS_DATA_URL
        )
    )

    ingest_transactions = PythonOperator(
        task_id='ingest_transactions',
        python_callable=ingest_data_callable,
        op_kwargs=dict(
            user=MONGO_USER,
            password=MONGO_PASSWORD,
            host=MONGO_HOST,
            port=MONGO_PORT,
            db=MONGO_DATABASE,
            table_name='Transaction',
            csv_file_url=TRANSACTIONS_DATA_URL
        )
    )

    ingest_book >> ingest_borrowers >> ingest_transactions



