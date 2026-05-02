# Importa o Flask para criar o server
from flask import Flask, request, jsonify
from flask_cors import CORS

# Cria o app
app = Flask(__name__)
CORS(app)

# Cria um BD (Inicialmente vazio)
storage = {}

# Define a rota '/document' que aceita o POST
@app.route("/document", methods=["POST"])
def document():

    # Pega os dados enviados em JSON
    data = request.get_json()

    # Retornar erro em modelo JSON, caso não haja dado
    if not data:
        return jsonify({"status": "error", "code": 400})

    # Extrai as informações do nosso JSON
    action = data.get("action")
    key = data.get("key")
    value = data.get("value")

    # Faz a criação e retorna em JSON 
    if action == "create":
        if key in storage:
            return jsonify({"status": "error", "code": 1})
        storage[key] = value
        return jsonify({"status": "ok", "code": 0})
        
    # Faz a atualização e retorna em JSON 
    if action == "update":
        if key not in storage:
            return jsonify({"status": "error", "code": 2})
        storage[key] = value
        return jsonify({"status": "ok", "code": 0})

    # Faz a remoção e retorna em JSON, apenas se a key existir ali no nosso BD...
    if action == "delete":
        if key not in storage:
            return jsonify({"status": "error", "code": 2})
        del storage[key]
        return jsonify({"status": "ok", "code": 0})

    return jsonify({"status": "error", "code": 402})


if __name__ == "__main__":
    app.run(debug=True)
