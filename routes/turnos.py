from flask import Blueprint, request, jsonify
from models import db, Turno

turnos_bp = Blueprint("turnos", __name__)

@turnos_bp.route("", methods=["POST"])
def crear_turno():
    data = request.json
    nuevo_turno = Turno(
        paciente=data['paciente'],
        email=data['email'],
        medico=data['medico'],
        fecha=data['fecha'],
        hora=data['hora']
    )
    db.session.add(nuevo_turno)
    db.session.commit()
    return jsonify({"mensaje": "Turno creado con éxito", "turno": nuevo_turno.to_dict()}), 201

@turnos_bp.route("", methods=["GET"])
def listar_turnos():
    turnos = Turno.query.all()
    return jsonify([t.to_dict() for t in turnos])

@turnos_bp.route("/<int:id>", methods=["GET"])
def obtener_turno(id):
    turno = Turno.query.get(id)
    if turno:
        return jsonify(turno.to_dict())
    return jsonify({"error": "Turno no encontrado"}), 404


@turnos_bp.route('/api/turnos/email/<string:email>', methods=['GET'])
def obtener_turnos_por_email(email):
    turnos = Turno.query.filter_by(email=email).all()
    if turnos:
        return jsonify([turno.to_dict() for turno in turnos])
    return jsonify([]), 200