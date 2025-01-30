import os

from src.data_handler import load_sql_file_to_dataframe

df = load_sql_file_to_dataframe(os.path.join("data","tickets.db"))

print(df.head())