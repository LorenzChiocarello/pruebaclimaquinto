from flask import Flask
from utils.db import app
from routes.valores_routes import valores_bp
from flask_cors import CORS

app.register_blueprint(valores_bp)

CORS(app)

if __name__ == '__main__':
    app.run(debug=True)
