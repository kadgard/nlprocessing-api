from app import app
from flask import jsonify
from flask import request
from services import NLProcessing

service = NLProcessing()


@app.route('/gram/<n>/texts', methods=['POST'])
def process_text(n):
    return bad_request(400) if int(n) <= 0 else service.process_texts(request.json, int(n))


@app.errorhandler(404)
def not_found():
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp


@app.errorhandler(400)
def bad_request():
    message = {
        'status': 400,
        'message': 'Bad Request: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 400

    return resp


if __name__ == "__main__":
    app.run()
