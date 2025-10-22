from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow frontend hosted elsewhere to access the API

# Temporary in-memory store (replace with DB later)
inventory = []
item_id = 1

@app.route("/inventory", methods=["GET"])
def get_inventory():
    return jsonify(inventory), 200

@app.route("/inventory", methods=["POST"])
def add_item():
    global item_id
    data = request.json
    if not data or "name" not in data or "quantity" not in data or "branch" not in data:
        return jsonify({"error": "Missing required fields"}), 400

    item = {
        "id": item_id,
        "name": data["name"],
        "quantity": data["quantity"],
        "branch": data["branch"]
    }
    inventory.append(item)
    item_id += 1
    return jsonify(item), 201

@app.route("/inventory/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    global inventory
    inventory = [i for i in inventory if i["id"] != item_id]
    return jsonify({"message": "Item deleted"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
