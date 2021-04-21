from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 33507))
    app.run(host='0.0.0.0', port=port)
