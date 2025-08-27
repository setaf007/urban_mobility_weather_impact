from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.operators.python import PythonOperator

def write_test_row():
    hook = PostgresHook(postgres_conn_id='analytics_postgres')
    hook.run("""
        CREATE TABLE IF NOT EXISTS dag_test (
            id SERIAL PRIMARY KEY,
            note TEXT,
            inserted_at TIMESTAMP DEFAULT now()
        );
        INSERT INTO dag_test (note) VALUES ('dag connectivity test');
    """)

default_args = {
    'owner': 'airflow',
}

dag = DAG(
    dag_id='test_postgres_conn',
    default_args=default_args,
    start_date=days_ago(1),
    schedule_interval=None,
    catchup=False
)

t1 = PythonOperator(
    task_id='write_row',
    python_callable=write_test_row,
    dag=dag
)