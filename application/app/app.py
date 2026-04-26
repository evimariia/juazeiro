from datetime import datetime
import flask
from application.database.connection import get_connection

app = flask.Flask(__name__)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)