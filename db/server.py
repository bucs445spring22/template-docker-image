from flask import Flask, request, jsonify
from tinydb import TinyDB


# Server
app = Flask(__name__)

# Database
db = TinyDB('db.json')


@app.route('/', methods=['GET'])
def index():
    return 'Hello, world!'


@app.route('/api/all', methods=['GET'])
def all():
    return jsonify(db.all())


@app.route('/api/save', methods=['POST'])
def save():
    # Bad request
    if request.headers['Content-Type'] != 'application/json':
        return jsonify(res='failure'), 400
    data = request.json
    db.insert(data)
    return jsonify(res='success', **data)


if __name__ ==  '__main__':
    app.run(host='0.0.0.0', port=5000)
