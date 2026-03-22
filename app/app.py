from flask import Flask
# from flask_cors import CORS
# from config import Config
# from models import db
from routes.usuarios import usuarios_bp
from routes.turnos import turnos_bp
from routes.profesionales import profesionales_bp

# app = Flask(__name__)
# app.config.from_object(Config)
# CORS(app)

# db.init_app(app)

# # Registramos los blueprints
# app.register_blueprint(usuarios_bp, url_prefix="/api/usuarios")
# app.register_blueprint(turnos_bp, url_prefix="/api/turnos")
# app.register_blueprint(profesionales_bp, url_prefix="/api/profesionales")

# with app.app_context():
#     db.create_all()

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000)


# from flask import Flask
# from routes.profesionales import profesionales_bp
# from routes.turnos import turnos_bp
# from routes.usuarios import usuarios_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(profesionales_bp)
    app.register_blueprint(turnos_bp)
    app.register_blueprint(usuarios_bp)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
