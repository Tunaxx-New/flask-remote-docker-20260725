from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def index():
    return jsonify(message="Hello from Flask on remote Docker!")


@app.get("/health")
def health():
    return jsonify(status="ok")
