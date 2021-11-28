from waitress import serve
from flask import Flask, jsonify
import os
from regenerator import Regenerator
from base64 import b64encode

salt = os.environ['REGEN_SALT']

regen = Regenerator(salt)
app = Flask(__name__)


@app.route('/<key>', methods=['GET'])
def regenerate(key):
    rsa = regen.regenerate_key(key)
    rsa_key = b64encode(rsa.exportKey(format='DER'))
    return jsonify({"result": True, "data": rsa_key.decode()})


if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=8001)
