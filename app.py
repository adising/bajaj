from flask import Flask, request, jsonify

app = Flask(__name__)

# Define the POST endpoint
@app.route('/bfhl', methods=['POST'])
def bfhl_post():
    data = request.json.get("data", [])
    
    # Separate numbers and alphabets
    numbers = [item for item in data if item.isdigit()]
    alphabets = [item for item in data if item.isalpha()]
    lowercase_alphabets = [item for item in alphabets if item.islower()]
    
    # Determine the highest lowercase alphabet
    highest_lowercase_alphabet = max(lowercase_alphabets) if lowercase_alphabets else None

    # Create the response
    response = {
        "is_success": True,
        "user_id": "john_doe_17091999",
        "email": "john@xyz.com",
        "roll_number": "ABCD123",
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": [highest_lowercase_alphabet] if highest_lowercase_alphabet else []
    }
    
    return jsonify(response), 200

# Define the GET endpoint
@app.route('/bfhl', methods=['GET'])
def bfhl_get():
    return jsonify({"operation_code": 1}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)
