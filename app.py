from flask import Flask
import logging
import json
import random
import time
from datetime import datetime
import threading

app = Flask(__name__)

# Configure the logger
logger = logging.getLogger('api_logger')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler('messages.log')
handler.setLevel(logging.DEBUG)

# Create a custom log format
formatter = logging.Formatter('{"time": "%(asctime)s", "level": "%(levelname)s", "message": %(message)s}')
handler.setFormatter(formatter)

logger.addHandler(handler)

# Simulate real-life transaction data
def generate_dummy_transaction():
    transaction = {
        "transaction_id": random.randint(100000, 999999),
        "user_id": random.randint(1000, 9999),
        "amount": round(random.uniform(10.0, 1000.0), 2),
        "currency": random.choice(["USD", "EUR", "GBP"]),
        "status": random.choice(["SUCCESS", "FAILED", "PENDING"]),
        "timestamp": datetime.utcnow().isoformat()
    }
    return json.dumps(transaction)

# Function to continuously generate logs
def continuous_log_generation():
    while True:
        transaction = generate_dummy_transaction()
        logger.debug(transaction)
        time.sleep(0.1)  # Adjust this to control log generation speed

# Start log generation in a separate thread
threading.Thread(target=continuous_log_generation, daemon=True).start()

@app.route('/')
def home():
    return "Flask logging app is running and generating logs!", 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
