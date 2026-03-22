from flask import Flask, app

from routes.env import env_bp
from routes.usuarios import usuarios_bp
from routes.turnos import turnos_bp
from routes.profesionales import profesionales_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(env_bp)
    app.register_blueprint(profesionales_bp)
    app.register_blueprint(turnos_bp)
    app.register_blueprint(usuarios_bp)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
