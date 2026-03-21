from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Turno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    paciente = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)    
    medico = db.Column(db.String(100), nullable=False)
    fecha = db.Column(db.String(10), nullable=False)
    hora = db.Column(db.String(5), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "paciente": self.paciente,
            "email": self.email,            
            "medico": self.medico,
            "fecha": self.fecha,
            "hora": self.hora
        }

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

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(255), unique=True, nullable=False)
    token_fcm = db.Column(db.String(500), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "token_fcm": self.token_fcm
        }
