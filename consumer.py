from kafka import KafkaConsumer
from pymongo import MongoClient
import json
import os

# Carregar configurações a partir das variáveis de ambiente
mongo_uri = os.getenv("MONGO_URI", "mongodb://root:example@mongodb:27017/")
kafka_bootstrap = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "kafka:9092")


# Conexão com MongoDB
mongo_client = MongoClient("mongodb://root:example@mongodb:27017/")
db = mongo_client["iot_db"]
collection = db["sensor_data"]

# Kafka Consumer
consumer = KafkaConsumer(
    'sensor_data',
    bootstrap_servers=kafka_bootstrap,
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print("Consumidor iniciado. Aguardando mensagens...")

for message in consumer:
    data = message.value
    print(f"Consumido: {data}")
    collection.insert_one(data)
    print("Inserção deu certo")
