import sqlite3
import pandas as pd

def load_csv_to_sqlite(csv_path, table_name, db_path="../database/nba.db"):
    df = pd.read_csv(csv_path)
    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()
    print(f"Loaded {csv_path} into table '{table_name}'")
