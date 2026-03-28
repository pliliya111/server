import os

from flask import Flask
from waitress import serve

app = Flask(__name__)

@app.route("/")
def index():
    return """<html>
    Привет от приложения Flask
    <br>
    <img src="static/orig.png">
    </html>
    """

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    # app.run(host='0.0.0.0', port=port)
    serve(app, host='0.0.0.0', port=port)