from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='static')
CORS(app)

@app.route('/greet', methods=['POST'])
def greet():
    data = request.json
    name = data.get('name', 'stranger')
    print({name})
    return jsonify({'message': f'Hello, {name}!'})

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
