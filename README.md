# Urban Mobility & Weather Impact Data Platform

## Overview
This project is an end-to-end data engineering platform designed to demonstrate real-world skills in:
- Batch + streaming ingestion (Kafka)
- Lakehouse (Delta) with Bronze → Silver → Gold
- Orchestration (Airflow)
- Analytics storage (PostgreSQL)
- Data quality (Great Expectations)
- Dashboards (Streamlit, Grafana) & log analytics (Kibana)

## Tech Stack
- Apache Kafka
- Apache Spark
- Apache Airflow
- PostgreSQL
- Delta Lake
- Grafana, Kibana, Streamlit

## Folder Structure
- **infra/** – Docker Compose & infra configs  
- **airflow/** – DAGs, logs, plugins  
- **producers/** – batch & streaming data producers  
- **spark_jobs/** – Spark batch/streaming jobs  
- **delta_store/** – local Delta tables (gitignored)  
- **postgres_schema/** – SQL schema & views  
- **ge/** – Great Expectations configs  
- **dashboards/** – Streamlit & Grafana assets  
- **tests/** – unit tests  
- **docs/** – diagrams & interview notes