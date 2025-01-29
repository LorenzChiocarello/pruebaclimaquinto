from flask import Flask
from utils.db import app
from routes.valores_routes import valores_bp

app.register_blueprint(valores_bp)

if __name__ == '__main__':
    app.run(debug=True)
