from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flasgger import Swagger
import os

app = Flask(__name__)
CORS(app)
swagger = Swagger(app)

# Configuración DB
db_url = os.environ.get('DATABASE_URL')
if db_url is None:
    db_url = 'sqlite:///turnos.db'
else:
    if db_url.startswith('postgres://'):
        db_url = db_url.replace('postgres://', 'postgresql://')

app.config['SQLALCHEMY_DATABASE_URI'] = db_url
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
    """
    Crear un nuevo turno médico
    ---
    tags:
      - Turnos
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              paciente:
                type: string
                example: "Juan Pérez"
              medico:
                type: string
                example: "Dra. López"
              fecha:
                type: string
                example: "2025-08-20"
              hora:
                type: string
                example: "10:30"
    responses:
      201:
        description: Turno creado con éxito
        content:
          application/json:
            schema:
              type: object
              properties:
                mensaje:
                  type: string
                turno:
                  type: object
                  properties:
                    id:
                      type: integer
                    paciente:
                      type: string
                    medico:
                      type: string
                    fecha:
                      type: string
                    hora:
                      type: string
    """
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
    """
    Obtener un turno por ID
    ---
    tags:
      - Turnos
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID del turno
    responses:
      200:
        description: Detalle del turno
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: integer
                paciente:
                  type: string
                medico:
                  type: string
                fecha:
                  type: string
                hora:
                  type: string
      404:
        description: Turno no encontrado
        content:
          application/json:
            schema:
              type: object
              properties:
                error:
                  type: string
    """
    turno = Turno.query.get(id)
    if turno:
        return jsonify(turno.to_dict())
    return jsonify({"error": "Turno no encontrado"}), 404

@app.route('/api/turnos/<int:id>', methods=['PUT'])
def modificar_turno(id):
    """
    Modificar un turno existente
    ---
    tags:
      - Turnos
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID del turno
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              paciente:
                type: string
                example: "Juan Pérez"
              medico:
                type: string
                example: "Dra. López"
              fecha:
                type: string
                example: "2025-08-20"
              hora:
                type: string
                example: "10:30"
    responses:
      200:
        description: Turno modificado con éxito
        content:
          application/json:
            schema:
              type: object
              properties:
                mensaje:
                  type: string
                turno:
                  type: object
                  properties:
                    id:
                      type: integer
                    paciente:
                      type: string
                    medico:
                      type: string
                    fecha:
                      type: string
                    hora:
                      type: string
      404:
        description: Turno no encontrado
        content:
          application/json:
            schema:
              type: object
              properties:
                error:
                  type: string
    """
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
    """
    Eliminar un turno por ID
    ---
    tags:
      - Turnos
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID del turno
    responses:
      200:
        description: Turno eliminado con éxito
        content:
          application/json:
            schema:
              type: object
              properties:
                mensaje:
                  type: string
      404:
        description: Turno no encontrado
        content:
          application/json:
            schema:
              type: object
              properties:
                error:
                  type: string
    """
    turno = Turno.query.get(id)
    if turno:
        db.session.delete(turno)
        db.session.commit()
        return jsonify({"mensaje": "Turno eliminado"})
    return jsonify({"error": "Turno no encontrado"}), 404

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)
