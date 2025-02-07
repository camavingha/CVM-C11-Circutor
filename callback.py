from flask import Flask, jsonify, send_from_directory
import random
import time
from threading import Thread
import os

app = Flask(__name__, static_folder='')

# Simulated meter readings
meter_data = {
    "current": 0.0,
    "voltage": 0.0,
    "power": 0.0,
    "timestamp": ""
}

def simulate_meter():
    while True:
        meter_data["current"] = round(random.uniform(0, 10), 2)
        meter_data["voltage"] = round(random.uniform(220, 240), 2)
        meter_data["power"] = round(meter_data["current"] * meter_data["voltage"], 2)
        meter_data["timestamp"] = time.strftime("%Y-%m-%d %H:%M:%S")
        time.sleep(2)

@app.route('/meter')
def get_meter_data():
    return jsonify(meter_data)

@app.route('/')
def serve_index():
    return send_from_directory(os.getcwd(), 'index.html')

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    # Start the simulation in a separate thread
    Thread(target=simulate_meter).start()
    app.run(debug=True, host='0.0.0.0', port=5000)

