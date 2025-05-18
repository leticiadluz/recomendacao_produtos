import yaml
import os
import pandas as pd
import snowflake.connector

path = os.path.join(os.path.dirname(__file__), "..", "include", "profiles.yml")

with open(path, "r") as f:
    profiles = yaml.safe_load(f)

profile_name = "recomendacao_produtos_dbt"
target = profiles[profile_name]["target"]
config = profiles[profile_name]["outputs"][target]

conn = snowflake.connector.connect(
    user=config["user"],
    password=config["password"],
    account=config["account"],
    warehouse=config["warehouse"],
    database=config["database"],
    schema=config["schema"],
    role=config.get("role", None)
)

query = "SELECT * FROM MART_PRODUTOS_TRANSACOES"
df_produtos = pd.read_sql(query, conn)
conn.close()

print(df_produtos.head())
