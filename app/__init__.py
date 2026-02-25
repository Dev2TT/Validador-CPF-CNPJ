from flask import Flask
from config import Config
from extensions import db
from app.routes.usuario_route import usuario_bp

def create_app():
    app=Flask(__name__)
    app.config.from_object(Config)

    try:
        db.init_app(app)
    except Exception as e:
        print(f'Nao foi possível inicializar o banco de dados {str(e.args)}')

    app.register_blueprint(usuario_bp)

    return app