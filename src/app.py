from flask import Flask, jsonify, request

app = Flask(__name__)

# Declare a global variable todos
todos = [
    {
        "label": "Sample",
        "done": True
    }
]

@app.route('/todos', methods=['POST'])
def add_new_todo():
    global todos
    request_body = request.json
    todos.append(request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This the pisiton to delete: ", position)
    todos.pop(position)
    return jsonify(todos)  

# Define the route and associated function for '/todos'
@app.route('/todos', methods=['GET'])
def todos_route():
    return jsonify(todos)

# Run the Flask app if this script is executed directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
