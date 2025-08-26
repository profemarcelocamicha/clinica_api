# APIs reserva de turnos
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


# Modelo Turno
class Turno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    paciente = db.Column(db.String(100), nullable=False)
    medico = db.Column(db.String(100), nullable=False)
    fecha = db.Column(db.String(10), nullable=False)
    hora = db.Column(db.String(5), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "paciente": self.paciente,
            "medico": self.medico,
            "fecha": self.fecha,
            "hora": self.hora
        }

@app.route('/api/turnos', methods=['POST'])
def crear_turno():
    data = request.json
    nuevo_turno = Turno(
        paciente=data['paciente'],
        medico=data['medico'],
        fecha=data['fecha'],
        hora=data['hora']
    )
    db.session.add(nuevo_turno)
    db.session.commit()
    return jsonify({"mensaje": "Turno creado con éxito", "turno": nuevo_turno.to_dict()}), 201

@app.route('/api/turnos/<int:id>', methods=['GET'])
def obtener_turno(id):
    turno = Turno.query.get(id)
    if turno:
        return jsonify(turno.to_dict())
    return jsonify({"error": "Turno no encontrado"}), 404

@app.route('/api/turnos/<int:id>', methods=['PUT'])
def modificar_turno(id):
    turno = Turno.query.get(id)
    if turno:
        data = request.json
        turno.paciente = data['paciente']
        turno.medico = data['medico']
        turno.fecha = data['fecha']
        turno.hora = data['hora']
        db.session.commit()
        return jsonify({"mensaje": "Turno modificado", "turno": turno.to_dict()})
    return jsonify({"error": "Turno no encontrado"}), 404

@app.route('/api/turnos/<int:id>', methods=['DELETE'])
def eliminar_turno(id):
    turno = Turno.query.get(id)
    if turno:
        db.session.delete(turno)
        db.session.commit()
        return jsonify({"mensaje": "Turno eliminado"})
    return jsonify({"error": "Turno no encontrado"}), 404


@app.route('/api/turnos', methods=['GET'])
def listar_turnos():
    turnos = Turno.query.all()
    return jsonify([turno.to_dict() for turno in turnos])


# @app.route('/api/tablas', methods=['GET'])
# def listar_tablas():
#     inspector = inspect(db.engine)
#     tablas = inspector.get_table_names()
#     return jsonify(tablas)

@app.route('/api/tablas', methods=['GET'])
def listar_tablas_seguras():
    tablas = ["turno", "profesional"]
    return jsonify(tablas)




# Modelo Profesional
class Profesional(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    fechaNac = db.Column(db.String(10), nullable=False)
    direccion = db.Column(db.String(100), nullable=False)

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





with app.app_context():
    # db.drop_all()   # elimina tablas existentes
    db.create_all() # crea todas las tablas con la definición actual



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


