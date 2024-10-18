from flask import make_response, jsonify

def json_response(data: dict, status_code: int):
    headers = {"Content-Type": "application/json"}
    return make_response(jsonify(data), status_code, headers)