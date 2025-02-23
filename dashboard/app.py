import streamlit as st
import pandas as pd
import psycopg2

import os


POSTGRES_DB = os.getenv("POSTGRES_DB", "stocks")
POSTGRES_USER = os.getenv("POSTGRES_USER", "user")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "password")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")

def fetch_data():
    conn = psycopg2.connect(
        dbname=POSTGRES_DB,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        host=POSTGRES_HOST,
        port=POSTGRES_PORT
    )
    df = pd.read_sql("SELECT * FROM stocks ORDER BY timestamp DESC LIMIT 100", conn)
    conn.close()
    return df

st.title("Real-Time Stock Price Dashboard")
data = fetch_data()
st.dataframe(data)
