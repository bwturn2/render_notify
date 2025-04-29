from flask import Flask, request, jsonify
import os
import json
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return "Notification Server is Running!"

@app.route('/healthz')
def health_check():
    return "OK", 200

@app.route('/notify', methods=['POST'])
def notify():
    data = request.json
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "event": data.get("event"),
        "message": data.get("message")
    }
    
    # Write log entry to events.log
    with open("events.log", "a") as log_file:
        log_file.write(json.dumps(log_entry) + "\n")
    
    return jsonify({"status": "received"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
