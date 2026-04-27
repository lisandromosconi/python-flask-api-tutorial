from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
    {"label": "choripan", "done": False},
    {"label": "pancho", "done": False}
]

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos), 200


@app.route('/todos', methods=['POST'])
def add_todo():
    new_todo = request.get_json()

    if not new_todo:
        return jsonify({"error": "No data"}), 400

    todos.append(new_todo)

    return jsonify(todos), 201

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):

    if position < 0 or position >= len(todos):
        return jsonify({"error": "Invalid position"}), 404

    todos.pop(position)

    return jsonify(todos), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)