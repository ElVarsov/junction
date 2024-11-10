from flask import Flask, request, jsonify

from flask_cors import CORS, cross_origin
import io
from PIL import Image
import base64
from ai import extract_details, extract_address
app = Flask(__name__)
import sql_handler
import json
import ifc_handler

# CORS(app, resources={r"/*": {"origins": "http://localhost:8081"}})


CORS(app)
@app.route('/')
def hello():
    return jsonify({"success": "Hello, World!"}), 200


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
    print("Received image...")
    data = request.json
    image_data = data.get('image')
    location = data.get('location')

    if image_data:
        processed_data = extract_details(image_data)
        response = {"status": processed_data}

        if location:
            response["location"] = extract_address(location["latitude"], location["longitude"])

        # Add entry to the database and get the entry ID
        entry_id = sql_handler.add_entry(response)
        response["entry_id"] = entry_id  # Include the entry ID in the response

        print(response)
        return jsonify(response), 200
    else:
        return jsonify({"error": "Image data not provided"}), 400
    

@app.route('/getentries', methods=['GET'])
def get_entries():
    data = sql_handler.get_entries()
    return jsonify(data), 200
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)




@app.route('/submit', methods=['POST'])
def submit():
    data = request.json

    location = (data["location_latitude"], data["location_longitude"])
    
    data.pop("location_latitude", None)
    data.pop("location_longitude", None)
    
    sql_handler.add_entry(data)
    
    print("added data: ", data)

    # update the IFC file
    ifc_handler.update_ifc_file(data, location)

    return jsonify({"success": "added!"}), 200



@app.route('/fetch', methods=['GET'])
def fetch():
    response = {"details": sql_handler.fetch_latest()}
    return jsonify(response), 200