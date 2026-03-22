# env.py
from flask import Blueprint, jsonify
import os

env_bp = Blueprint("env", __name__)

@env_bp.route("/env")
def env():
    return jsonify({
        "ENV": os.getenv("ENV"),
        "DEBUG": os.getenv("DEBUG")
    })