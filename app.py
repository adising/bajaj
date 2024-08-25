from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes and origins

@app.route('/bfhl', methods=['POST'])
def handle_post():
    try:
        # Extract the input data from the request
        data = request.json
        input_data = data.get('data', [])  # Adjust the key based on your frontend

        # Initialize lists for numbers and alphabets
        numbers = [item for item in input_data if item.isdigit()]
        alphabets = [item for item in input_data if item.isalpha()]
        highest_lowercase_alphabet = [max([ch for ch in alphabets if ch.islower()], default='')]

        # Construct the response
        response = {
            "is_success": True,
            "user_id": "john_doe_17091999",
            "email": "john@xyz.com",
            "roll_number": "ABCD123",
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": highest_lowercase_alphabet
        }

        return jsonify(response), 200
    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 500

@app.route('/bfhl', methods=['GET'])
def handle_get():
    return jsonify({"operation_code": 1})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
