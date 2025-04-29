from flask import Flask, request, jsonify
import os
import datetime

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

    # Log event to file
    with open('events.log', 'a') as f:
        timestamp = datetime.datetime.now().isoformat()
        f.write(f"{timestamp} - Event: {data.get('event')} - Message: {data.get('message')}\n")

    return jsonify({'status': 'received'}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
