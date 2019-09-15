from app import app
from flask import request



@app.route('/', methods=['POST'])
def process_text():
    return 'Foi minunu!'

if __name__ == "__main__":
    app.run()