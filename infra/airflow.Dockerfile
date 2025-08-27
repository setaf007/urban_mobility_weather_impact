FROM apache/airflow:2.8.0

COPY requirements-airflow.txt /requirements-airflow.txt

USER airflow
RUN pip install --no-cache-dir -r /requirements-airflow.txt
