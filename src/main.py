import requests

from flask import Flask
app = Flask(__name__)

@app.route('/')
def ping():
    return 'success'

@app.route('/get')
def get():
    content = requests.get("http://bloom-public-test-bucket.s3.amazonaws.com/dummy")
    return content.content.decode('utf-8')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')