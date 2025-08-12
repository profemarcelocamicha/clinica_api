from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_restx import Api, Resource, fields
import os

app = Flask(__name__)
CORS(app)
api = Api(app, version='1.0', title='API Turnos Médicos',
          description='API para gestión de turnos con documentación Swagger')

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

# Modelo DB
class Turno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    paciente = db.Column(db.String(100), nullable=False)
    medico = db.Column(db.String(100), nullable=False)
    fecha = db.Column(db.String(10), nullable=False)
    hora = db.Column(db.String(5), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'paciente': self.paciente,
            'medico': self.medico,
            'fecha': self.fecha,
            'hora': self.hora
        }

# Modelo para Swagger (esquema de datos)
turno_model = api.model('Turno', {
    'id': fields.Integer(readonly=True, description='ID del turno'),
    'paciente': fields.String(required=True, description='Nombre del paciente'),
    'medico': fields.String(required=True, description='Nombre del médico'),
    'fecha': fields.String(required=True, description='Fecha del turno (YYYY-MM-DD)'),
    'hora': fields.String(required=True, description='Hora del turno (HH:MM)')
})

ns = api.namespace('turnos', description='Operaciones sobre turnos')

@ns.route('/')
class TurnoList(Resource):
    @ns.marshal_list_with(turno_model)
    def get(self):
        """Listar todos los turnos"""
        turnos = Turno.query.all()
        return [t.to_dict() for t in turnos]

    @ns.expect(turno_model, validate=True)
    @ns.marshal_with(turno_model, code=201)
    def post(self):
        """Crear un nuevo turno"""
        data = api.payload
        nuevo_turno = Turno(
            paciente=data['paciente'],
            medico=data['medico'],
            fecha=data['fecha'],
            hora=data['hora']
        )
        db.session.add(nuevo_turno)
        db.session.commit()
        return nuevo_turno.to_dict(), 201

@ns.route('/<int:id>')
@ns.response(404, 'Turno no encontrado')
@ns.param('id', 'ID del turno')
class TurnoResource(Resource):
    @ns.marshal_with(turno_model)
    def get(self, id):
        """Obtener turno por ID"""
        turno = Turno.query.get_or_404(id)
        return turno.to_dict()

    @ns.expect(turno_model, validate=True)
    @ns.marshal_with(turno_model)
    def put(self, id):
        """Modificar un turno existente"""
        turno = Turno.query.get_or_404(id)
        data = api.payload
        turno.paciente = data['paciente']
        turno.medico = data['medico']
        turno.fecha = data['fecha']
        turno.hora = data['hora']
        db.session.commit()
        return turno.to_dict()

    def delete(self, id):
        """Eliminar un turno"""
        turno = Turno.query.get_or_404(id)
        db.session.delete(turno)
        db.session.commit()
        return {'mensaje': 'Turno eliminado'}

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)
