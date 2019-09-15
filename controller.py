from app import app
from flask import jsonify
from flask import request

@app.route('/', methods=['POST'])
def process_text():
    return 'Foi minunu!'

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

@app.errorhandler(400)
def bad_request(error=None):
    message = {
        'status': 400,
        'message': 'Bad Request: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 400

    return resp

if __name__ == "__main__":
    app.run()
