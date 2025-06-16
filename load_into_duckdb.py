import duckdb
import pandas as pd

df = pd.read_csv("data/processed/marketing_campaign_cleaned.csv")

#connect to or create DuckDB database for superset
con = duckdb.connect("superset_duck.db")

df.to_sql("marketing_data", con, if_exists='replace', index=False)

print("Table 'marketing_data' loaded into superset_duck.db")
