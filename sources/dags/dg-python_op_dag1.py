from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
from py_operator_dag_tasks.task1 import task1
from py_operator_dag_tasks.task2 import task2
from py_operator_dag_tasks.task3 import task3




default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 11, 11),
    'retries': 1
}

# Define the DAG
with DAG(
    dag_id='dg-python_operator_dag1',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False
) as dag:
    
    # Define the PythonOperator task
    python_task1 = PythonOperator(
        task_id='create_df_and_save',
        python_callable=task1
    )

    python_task2 = PythonOperator(
    task_id='read_df_and_transform',
    python_callable=task2
    )

    python_task3 = PythonOperator(
    task_id='filter_df',
    python_callable=task3
    )

# Set task dependencies (only one task in this case)
python_task1 >> python_task2 >> python_task3