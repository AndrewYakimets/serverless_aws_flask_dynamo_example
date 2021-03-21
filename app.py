import os
import uuid
import datetime as dt

import boto3
from flask import Flask, jsonify, request

app = Flask(__name__)

COORDINATES_TABLE = os.environ['COORDINATES_TABLE']
IS_OFFLINE = os.environ.get('IS_OFFLINE')
client = boto3.client('dynamodb', region_name="eu-central-1")

if IS_OFFLINE:
    client = boto3.client(
        'dynamodb',
        region_name='localhost',
        endpoint_url='http://localhost:8000'
    )
else:
    client = boto3.client('dynamodb')


@app.route("/")
def test():
    return jsonify({"message": "All is ok!"}), 200


@app.route("/coordinates", methods=["POST"])
def create_coordinates():
    coordinates_id = str(uuid.uuid4())
    latitude = request.json.get('latitude')
    longitude = request.json.get('longitude')
    record_date = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if not latitude:
        return jsonify({"message": "Please provide latitude!"}), 400
    elif not longitude:
        return jsonify({"message": "Please provide longitude!"}), 400

    client.put_item(
        TableName=COORDINATES_TABLE,
        Item={
            'coordinates_id': {'S': coordinates_id},
            'latitude': {'S': latitude},
            'longitude': {'S': longitude},
            'record_date': {'S': record_date}
        }
    )

    return jsonify({"message": "created!"}), 201
