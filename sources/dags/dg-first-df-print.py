from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd

# Define a function that creates a dummy dataframe and prints it
def create_and_print_dataframe():
    # Create a dummy dataframe
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [24, 27, 22, 32],
        'Country': ['USA', 'Canada', 'UK', 'Australia']
    }
    df = pd.DataFrame(data)
    
    # Print the dataframe
    print("Generated DataFrame:")
    print(df)

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 10, 12),
    'retries': 1
}

# Define the DAG
with DAG(
    dag_id='dummy_dataframe_dag',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False
) as dag:
    
    # Define the PythonOperator task
    print_dataframe_task = PythonOperator(
        task_id='print_dataframe_task',
        python_callable=create_and_print_dataframe
    )

# Set task dependencies (only one task in this case)
print_dataframe_task
    