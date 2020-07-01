from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'ITVersity, Inc',
    'start_date': days_ago(2)
}

dag = DAG(
    dag_id='etl_demo_101',
    default_args=default_args,
    schedule_interval='0 0 * * *',
    catchup=False
)

create_orders_dir = BashOperator(
    task_id='create_orders_dir',
    bash_command='mkdir -p /tmp/orders',
    dag=dag
)

create_customers_dir = BashOperator(
    task_id='create_customers_dir',
    bash_command='mkdir -p /tmp/customers',
    dag=dag
)

create_join_dir = BashOperator(
    task_id='create_join_dir',
    bash_command='mkdir -p /tmp/join_orders_and_customers',
    dag=dag
)

get_orders_from_mysql = BashOperator(
    task_id='get_orders_from_mysql',
    bash_command='/home/dgadiraju/airflow/dags/fetch_orders.sh ',
    dag=dag
)

get_customers_from_pg = BashOperator(
    task_id='get_customers_from_pg',
    bash_command='export CUSTOMER_DB_USER=retail_user;export CUSTOMER_DB_PASS=itversity;/home/dgadiraju/etl-demo/etl-demo-env/bin/python /home/dgadiraju/etl-demo/app.py dev CUSTOMER_DB customers',
    dag=dag
)

join_orders_and_customers = BashOperator(
    task_id='join_orders_and_customers',
    bash_command='/home/dgadiraju/etl-demo/etl-demo-env/bin/python /home/dgadiraju/etl-demo/process.py',
    dag=dag
)

drop_orders_dir = BashOperator(
    task_id='drop_orders_dir',
    bash_command='rm -rf /tmp/orders',
    dag=dag
)

drop_customers_dir = BashOperator(
    task_id='drop_customers_dir',
    bash_command='rm -rf /tmp/customers',
    dag=dag
)

create_orders_dir >> get_orders_from_mysql >> join_orders_and_customers
create_customers_dir >> get_customers_from_pg >> join_orders_and_customers
create_join_dir >> join_orders_and_customers

join_orders_and_customers >> drop_orders_dir
join_orders_and_customers >> drop_customers_dir

if __name__ == "__main__":
    dag.cli()