from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

storage = {}

@app.route("/document", methods=["POST"])
def document():
    data = request.get_json()

    if not data:
        return jsonify({"status": "error", "code": 400})

    action = data.get("action")
    key = data.get("key")
    value = data.get("value")

    if not action or not key:
        return jsonify({"status": "error", "code": 401})

    if action == "create":
        if key in storage:
            return jsonify({"status": "error", "code": 1})
        storage[key] = value
        return jsonify({"status": "ok", "code": 0})

    if action == "update":
        if key not in storage:
            return jsonify({"status": "error", "code": 2})
        storage[key] = value
        return jsonify({"status": "ok", "code": 0})

    if action == "delete":
        if key not in storage:
            return jsonify({"status": "error", "code": 2})
        del storage[key]
        return jsonify({"status": "ok", "code": 0})

    return jsonify({"status": "error", "code": 402})


if __name__ == "__main__":
    app.run(debug=True)