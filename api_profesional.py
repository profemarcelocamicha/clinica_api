# APIs reserva de profesional
import inspect
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Configuración de la base de datos desde variable de entorno
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# Modelo Profesional
class Profesional(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    fechaNac = db.Column(db.String(10), nullable=False)
    dirección = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "fechaNac": self.fechaNac,
            "direccion": self.direccion
        }

@app.route('/api/profesional', methods=['POST'])
def crear_profesional():
    data = request.json
    nuevo_profesional = Profesional(
        nombre=data['nombre'],
        apellido=data['apellido'],
        fechaNac=data['fechaNac'],
        direccion=data['direccion']
    )
    db.session.add(nuevo_profesional)
    db.session.commit()
    return jsonify({"mensaje": "profesional creado con éxito", "profesional": nuevo_profesional.to_dict()}), 201

@app.route('/api/profesional/<int:id>', methods=['GET'])
def obtener_profesional(id):
    profesional = Profesional.query.get(id)
    if profesional:
        return jsonify(profesional.to_dict())
    return jsonify({"error": "profesional no encontrado"}), 404

@app.route('/api/profesional/<int:id>', methods=['PUT'])
def modificar_profesional(id):
    profesional = Profesional.query.get(id)
    if profesional:
        data = request.json
        profesional.nombre = data['nombre']
        profesional.apellido = data['apellido']
        profesional.fechaNac = data['fechaNac']
        profesional.direccion = data['direccion']
        db.session.commit()
        return jsonify({"mensaje": "profesional modificado", "profesional": profesional.to_dict()})
    return jsonify({"error": "profesional no encontrado"}), 404

@app.route('/api/profesional/<int:id>', methods=['DELETE'])
def eliminar_profesional(id):
    profesional = Profesional.query.get(id)
    if profesional:
        db.session.delete(profesional)
        db.session.commit()
        return jsonify({"mensaje": "profesional eliminado"})
    return jsonify({"error": "profesional no encontrado"}), 404


@app.route('/api/profesional', methods=['GET'])
def listar_profesional():
    profesional = Profesional.query.all()
    return jsonify([profesional.to_dict() for profesional in profesional])


@app.route('/api/tablas', methods=['GET'])
def listar_tablas():
    inspector = inspect(db.engine)
    tablas = inspector.get_table_names()
    return jsonify(tablas)


with app.app_context():
    db.create_all()



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


