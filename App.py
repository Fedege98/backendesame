from flask import Flask, request, jsonify
from azure.iot.hub import IoTHubRegistryManager
from azure.iot.hub.models import CloudToDeviceMethod, CloudToDeviceMethodResult
from flask_cors import CORS
import json
app = Flask(__name__)

CORS(app)

@app.route('/sendToIoTHub', methods=['POST'])
def send_to_iothub():
    codice = request.json.get('time')

    CONNECTION_STRING = "HostName=ERAAIotHub.azure-devices.net;SharedAccessKeyName=iothubowner;SharedAccessKey=GWkzgEGpfMNjP2rIIEmUqsooLIc3oDbKfq1+3cxN5pU="
    DEVICE_ID = "ERAAGateway1"

    registry_manager = IoTHubRegistryManager(CONNECTION_STRING)
    message_json = {"time": codice}
    registry_manager.send_c2d_message(DEVICE_ID, json.dumps(message_json))

    print(f"inviato {codice}")

    return jsonify({'time': codice})





