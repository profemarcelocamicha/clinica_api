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


@app.route('/api/tablas', methods=['GET'])
def listar_tablas():
    inspector = inspect(db.engine)
    tablas = inspector.get_table_names()
    return jsonify(tablas)





with app.app_context():
    db.create_all()



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


