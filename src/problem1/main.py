# I created this file to mock the API response for the problem
from flask import Flask, jsonify

app = Flask(__name__)

# Mock data to simulate responses for specific order IDs
mock_responses = {
    "12346": {"order_id": "12346", "status": "success", "message": "Order details for TSLA"},
    "12362": {"order_id": "12362", "status": "success", "message": "Order details for TSLA"},
}

@app.route('/api/:<order_id>', methods=['GET'])
def get_order(order_id):
    # Check if the order_id exists in the mock data
    if order_id in mock_responses:
        return jsonify(mock_responses[order_id]), 200
    else:
        return jsonify({"error": "Order not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)