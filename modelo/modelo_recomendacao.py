import yaml
import os
import pandas as pd
from sqlalchemy.engine import create_engine
from urllib.parse import quote_plus
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

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

lista_produtos = df_produtos["nomes_produtos"].apply(lambda x: [item.strip() for item in x.split(",")]).tolist()

print(lista_produtos[0:5])

te = TransactionEncoder()
te_ary = te.fit(lista_produtos).transform(lista_produtos)
print(te_ary[0:5])

print(te.columns_)

df_lista_produtos = pd.DataFrame(te_ary, columns=te.columns_)
print(df_lista_produtos.head())

frequent_itemsets = apriori(df_lista_produtos, min_support=0.01, use_colnames=True)
print(frequent_itemsets)

rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.5)
print(rules[["antecedents", "consequents", "support", "confidence", "lift"]].sort_values(by="lift", ascending=False))



