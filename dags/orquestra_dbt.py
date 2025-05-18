from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

REPO_URL = "https://github.com/leticiadluz/recomendacao_produtos_dbt.git"
DBT_DIR = "/tmp/dbt_project"

with DAG(
    dag_id="orquestra_dbt",
    schedule=None,
    start_date=datetime(2025, 5, 17),
    catchup=False,
    tags=["dbt", "git"]
) as dag:

    clone_repo = BashOperator(
        task_id="clone_dbt_repo",
        bash_command=f"rm -rf {DBT_DIR} && git clone {REPO_URL} {DBT_DIR}"
    )

    dbt_deps = BashOperator(
        task_id="dbt_deps",
        bash_command=f"dbt deps --project-dir {DBT_DIR} --profiles-dir /home/astro/.dbt"
    )

    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command=f"dbt run --project-dir {DBT_DIR} --profiles-dir /home/astro/.dbt"
    )

    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command=f"dbt test --project-dir {DBT_DIR} --profiles-dir /home/astro/.dbt"
    )

    clone_repo >> dbt_deps >> dbt_run >> dbt_test
