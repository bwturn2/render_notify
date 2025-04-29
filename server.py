from flask import Flask, request, jsonify
from datetime import datetime
import os
import json

app = Flask(__name__)

@app.route('/')
def home():
    return "Notification Server is Running!"

@app.route('/healthz')
def health_check():
    return "OK", 200

@app.route('/notify', methods=['POST'])
def notify():
    data = request.get_json()
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "event": data.get("event", "unknown"),
        "message": data.get("message", "")
    }
    with open("events.log", "a") as f:
        f.write(json.dumps(log_entry) + "\n")
    return jsonify({"status": "received"})

@app.route('/logs', methods=['GET'])
def get_logs():
    if not os.path.exists("events.log"):
        return jsonify({"error": "Log file not found"}), 404
    with open("events.log", "r") as f:
        lines = f.readlines()
        logs = [json.loads(line.strip()) for line in lines]
    return jsonify({"logs": logs})

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.get_json()
        log_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "event": "webhook_event",
            "data": data
        }
        with open("events.log", "a") as f:
            f.write(json.dumps(log_entry) + "\n")
        return jsonify({"status": "webhook received"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
