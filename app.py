import json

from flask import Flask

app = Flask(__name__)


@app.route('/hello')
def hello():
    resp = {
        'status': 'OK'
    }
    return json.dumps(resp)


if __name__ == '__main__':
    app.run()
