from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.operators.python import PythonOperator

def delete_test_rows():
    hook = PostgresHook(postgres_conn_id='analytics_postgres')
    hook.run("DELETE FROM dag_test WHERE note = 'dag connectivity test';")

default_args = {
    'owner': 'airflow',
}

dag = DAG(
    dag_id='delete_test_rows',
    default_args=default_args,
    start_date=days_ago(1),
    schedule_interval=None,
    catchup=False
)

t1 = PythonOperator(
    task_id='delete_rows',
    python_callable=delete_test_rows,
    dag=dag
)