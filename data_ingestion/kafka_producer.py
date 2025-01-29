from kafka import KafkaProducer
import json
import time
import requests

import os
import json
import time
import requests
from kafka import KafkaProducer

KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "stock_prices")
KAFKA_SERVER = os.getenv("KAFKA_SERVER", "localhost:9092")
STOCK_API_URL = os.getenv("STOCK_API_URL", "https://api.example.com/stock_prices")

def fetch_stock_data():
    response = requests.get(STOCK_API_URL)
    return response.json()

def main():
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_SERVER,
        value_serializer=lambda v: json.dumps(v).encode("utf-8")
    )
    while True:
        stock_data = fetch_stock_data()
        producer.send(KAFKA_TOPIC, stock_data)
        time.sleep(5)

if __name__ == "__main__":
    main()