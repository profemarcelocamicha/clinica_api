import os
import shutil

BASE_DIR = os.getcwd()

# Archivos que NO se deben mover
EXCLUDE_FILES = {
    "app.py",  # lo tratamos aparte
    "reorganizar_proyecto.py"
}

EXCLUDE_DIRS = {
    "venv",
    ".git",
    ".github",
    "tests",
    "routes",
    "__pycache__"
}

APP_DIR = os.path.join(BASE_DIR, "app")

# Crear carpeta app si no existe
os.makedirs(APP_DIR, exist_ok=True)

print("📁 Creando estructura...")

# Mover archivos .py a app/
for file in os.listdir(BASE_DIR):
    full_path = os.path.join(BASE_DIR, file)

    if os.path.isfile(full_path) and file.endswith(".py"):
        if file not in EXCLUDE_FILES:
            print(f"➡️ Moviendo {file} a app/")
            shutil.move(full_path, os.path.join(APP_DIR, file))

# Crear __init__.py en app/
init_file = os.path.join(APP_DIR, "__init__.py")
if not os.path.exists(init_file):
    with open(init_file, "w") as f:
        f.write("# Inicialización del paquete app\n")

# Crear __init__.py en routes si no existe
routes_init = os.path.join(BASE_DIR, "routes", "__init__.py")
if not os.path.exists(routes_init):
    with open(routes_init, "w") as f:
        f.write("# Inicialización de rutas\n")

# Crear requirements-dev.txt
dev_requirements = os.path.join(BASE_DIR, "requirements-dev.txt")

with open(dev_requirements, "w") as f:
    f.write("""-r requirements.txt

pytest
pytest-cov
""")

print("✅ Reorganización completada")
print("⚠️ Ahora tenés que ajustar imports (te explico abajo)")