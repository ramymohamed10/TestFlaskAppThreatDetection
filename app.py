from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Configure basic logging
logging.basicConfig(level=logging.INFO)

@app.route('/')
def home():
    app.logger.info('Home page accessed')
    return "Hello from Azure Flask App!"

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username == "admin" and password == "password":
        app.logger.info(f'Successful login for user: {username}')
        return jsonify({"message": "Login successful"}), 200
    else:
        app.logger.warning(f'Failed login attempt for user: {username}')
        return jsonify({"message": "Invalid credentials"}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)