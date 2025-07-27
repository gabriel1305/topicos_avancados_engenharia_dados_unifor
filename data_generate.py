from faker import Faker
import random
import datetime

fake = Faker()

def generate_sensor_data():
    return {
        "sensor_id": fake.uuid4(),
        "temperature": round(random.uniform(20.0, 40.0), 2),
        "humidity": round(random.uniform(30.0, 80.0), 2),
        "timestamp": datetime.datetime.now().isoformat()
    }

for i in range(1,10,1):
    print(generate_sensor_data())
