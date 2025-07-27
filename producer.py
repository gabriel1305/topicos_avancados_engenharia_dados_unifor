from kafka import KafkaProducer
import json
import time
from data_generate import generate_sensor_data
import os

bootstrap_servers = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "kafka:9092")

producer = KafkaProducer(
    bootstrap_servers=bootstrap_servers,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')  # ✅ SERIALIZADOR ADICIONADO
)

TOPIC = 'sensor_data'

if __name__ == "__main__":
    while True:
        data = generate_sensor_data()
        print(f"Enviando: {data}")
        producer.send(TOPIC, value=data)
        time.sleep(2)
