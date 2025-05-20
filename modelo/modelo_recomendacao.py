import yaml
import os
import pandas as pd
from sqlalchemy.engine import create_engine
from urllib.parse import quote_plus

path = os.path.join(os.path.dirname(__file__), "..", "include", "profiles.yml")
with open(path, "r") as f:
    profiles = yaml.safe_load(f)

profile_name = "recomendacao_produtos_dbt"
target = profiles[profile_name]["target"]
config = profiles[profile_name]["outputs"][target]

user = config["user"]
password = quote_plus(config["password"])
account = config["account"]
warehouse = config["warehouse"]
database = config["database"]
schema = config["schema"]
role = config.get("role", "")

conn_str = f"snowflake://{user}:{password}@{account}/{database}/{schema}?warehouse={warehouse}"
if role:
    conn_str += f"&role={role}"

engine = create_engine(conn_str)

query = "SELECT * FROM MART_PRODUTOS_TRANSACOES"
df_produtos = pd.read_sql(query, engine)

print(df_produtos.head())
