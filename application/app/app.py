from datetime import datetime
from flask import Flask
from application.database.connection import get_connection

app = Flask(__name__)
# app.debug = True

# # Import routes to register them
from application.app.routes.presenca_routes import auth_presenca_rota

app.register_blueprint(auth_presenca_rota)

@app.route('/')
def home():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)