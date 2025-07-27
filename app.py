import streamlit as st
import pandas as pd
from pymongo import MongoClient
import time

st.title("📊 Monitoramento em Tempo Real - Sensores IoT")

client = MongoClient("mongodb://root:example@mongodb:27017/")
db = client["iot_db"]
collection = db["sensor_data"]

st.write("Atualizando dados em tempo real...")

placeholder = st.empty()

while True:
    data = list(collection.find().sort("timestamp", -1).limit(20))
    df = pd.DataFrame(data)
    if not df.empty:
        df = df[["sensor_id", "temperature", "humidity", "timestamp"]]
        placeholder.dataframe(df, use_container_width=True)
    time.sleep(2)
