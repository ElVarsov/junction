from flask import Flask, request, jsonify

from flask_cors import CORS, cross_origin
import io
from PIL import Image
import base64
from ai import extract_details

app = Flask(__name__)
# CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

@app.route('/')
def hello():
    return 'Hello, World'


@app.route("/hi", methods=["POST"])
def hi():
    data = request.get_json()
    if data and "name" in data:
        name = data["name"]
        return jsonify({"hello": name}), 200
    else:
        return jsonify({"error": "Name not provided"}), 400
    

@app.route('/process', methods=['POST'])
def upload_image():
    data = request.json
    image_data = data.get('image')
    if image_data:
        data = extract_details(image_data)
        return jsonify({"status": data}), 200
    else:
        return jsonify({"status": "failure", "reason": "No image data"}), 400