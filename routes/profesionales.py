from flask import Blueprint, request, jsonify
from models import db, Profesional

profesionales_bp = Blueprint("profesionales", __name__)

@profesionales_bp.route("", methods=["POST"])
def crear_profesional():
    data = request.json
    nuevo = Profesional(
        nombre=data['nombre'],
        apellido=data['apellido'],
        fechaNac=data['fechaNac'],
        direccion=data['direccion']
    )
    db.session.add(nuevo)
    db.session.commit()
    return jsonify({"mensaje": "Profesional creado", "profesional": nuevo.to_dict()})

@profesionales_bp.route("", methods=["GET"])
def listar_profesionales():
    profes = Profesional.query.all()
    return jsonify([p.to_dict() for p in profes])
