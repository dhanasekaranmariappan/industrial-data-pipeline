import pandas as pd
from .db import connect

def fetch_data():
    conn = connect()
    df = pd.read_sql("SELECT * FROM machine_data", conn)
    conn.close()
    return df

def failure_patterns(df):
    print(df.groupby("tool_wear")["power"].mean())
