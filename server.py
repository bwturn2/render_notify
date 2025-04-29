from flask import Flask, request
import os

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
    print("Notification received:", data)
    return {"status": "success", "message": "Notification received"}, 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
