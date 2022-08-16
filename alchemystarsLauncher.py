import os
from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

dgpapi = "https://apidgp-gameplayer.games.dmm.com/"

@app.route('/dmmapi/', defaults={'path': ''})
@app.route('/dmmapi/<path:path>', methods=['GET','POST'])
def dmmapi(path):
    resp = requests.request(method=request.method, url = dgpapi + path, headers=request.headers, json=request.get_json())
    return jsonify(resp.json())

app.run(debug=False, port=9000, host='0.0.0.0')