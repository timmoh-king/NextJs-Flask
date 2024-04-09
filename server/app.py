from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/api/home",  methods=['GET'])
def welcome_home():
    return jsonify({
        "message": "Hello welcome home",
        "people": ['John', 'Doe', 'Alex']
    })


if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')
