from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes and origins

@app.route('/bfhl', methods=['POST'])
def handle_post():
    data = request.json
    # Process data here
    response = {
        "is_success": True,
        "user_id": "john_doe_17091999",
        "email": "john@xyz.com",
        "roll_number": "ABCD123",
        "numbers": [],
        "alphabets": [],
        "highest_lowercase_alphabet": []
    }
    return jsonify(response)

@app.route('/bfhl', methods=['GET'])
def handle_get():
    return jsonify({"operation_code": 1})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
