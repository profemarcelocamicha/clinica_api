from flask import Blueprint, request, jsonify
from models import db, Usuario
from services.notifications import enviar_notificacion

usuarios_bp = Blueprint("usuarios", __name__)


@usuarios_bp.route("", methods=["POST"])
def crear_usuario():
    data = request.json
    nuevo_usuario = Usuario(
        user_id=data['userId'],
        token_fcm=data['token_fcm'],
    )
    db.session.add(nuevo_usuario)
    db.session.commit()
    return jsonify({"mensaje": "Usuario creado con éxito", "Usuario": nuevo_usuario.to_dict()}), 201



@usuarios_bp.route("/token", methods=["POST"])
def guardar_token_usuario():
    data = request.form
    user_id = data.get("userId")
    token = data.get("token")

    if not user_id or not token:
        return jsonify({"status": "error", "message": "Faltan datos"}), 400

    usuario = Usuario.query.filter_by(user_id=user_id).first()
    if usuario:
        usuario.token_fcm = token
    else:
        usuario = Usuario(user_id=user_id, token_fcm=token)
        db.session.add(usuario)

    db.session.commit()
    return jsonify({"status": "ok", "message": "Token guardado correctamente"})

@usuarios_bp.route("/notificar", methods=["POST"])
def notificar_usuario():
    data = request.json
    user_id = data.get("userId")
    titulo = data.get("titulo", "Notificación")
    cuerpo = data.get("cuerpo", "Mensaje desde la clínica")

    usuario = Usuario.query.filter_by(user_id=user_id).first()
    if not usuario:
        return jsonify({"status": "error", "message": "Usuario no encontrado"}), 404

    result = enviar_notificacion(usuario.token_fcm, titulo, cuerpo)
    return jsonify({"status": "ok", "resultado": result})

@usuarios_bp.route("/listar", methods=["GET"])
def listar_usuarios():
    from models import Usuario
    usuarios = Usuario.query.all()
    return {
        "usuarios": [u.to_dict() for u in usuarios]
    }
