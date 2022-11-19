#import libraries

from datetime import timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago


#DAG arguments
default_args = {
    'owner' : 'John Smith',
    'start_date' : days_ago(0),
    'email' : ['john@something.com'],
    'email_on_failure' : True,
    'email_on_retry' : True,
    'retries' : 1,
    'retry_delay' : timedelta(seconds=30), 
}

#DAG definition

dag = DAG (
    dag_id = 'process_web_log',
    default_args = default_args,
    description = 'analyzes the log file, executes ETL',
    schedule_interval = timedelta(days=1),
                   
)


#task definition

extract_data = BashOperator (
    task_id = 'extract_data',
    bash_command = 'grep -o "[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\} "\
                    /home/project/airflow/dags/capstone/accesslog.txt > \
                    /home/project/airflow/dags/capstone/extracted_data.txt',
    dag = dag,
)

#define second task

transform_data = BashOperator(
    task_id = 'transform_data',
    bash_command = 'grep -o "198.46.149.143 "\
                    /home/project/airflow/dags/capstone/extracted_data.txt > \
                    /home/project/airflow/dags/capstone/transformed_data.txt',
    dag = dag,
)

#define third task

load_data = BashOperator (
    task_id = 'load_data',
    bash_command = 'tar -czvf /home/project/airflow/dags/capstone/weblog.tar \
                    /home/project/airflow/dags/capstone/transformed_data.txt',
    dag = dag,
)

#task pipeline
extract_data >> transform_data >> load_data

