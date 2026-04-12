import multiprocessing
import webview
import time
from pathlib import Path
from flask import Flask, send_from_directory, abort, jsonify
from python.flask.blueprints.project import project_blueprint
from python.flask.api.api import Api

# ==================== CONFIGURACIÓN FLASK ====================
# Ajustamos la ruta correctamente
BASE_DIR = Path(__file__).resolve().parent       # carpeta donde está main.py (src/)
HTML_DIR = BASE_DIR / "server"                   # carpeta con index.html, Cesium, styles, etc.

app = Flask(__name__)

# ====================== RUTA PRINCIPAL ======================
@app.route('/')
def index():
    try:
        return send_from_directory(str(HTML_DIR), 'index.html')
    except FileNotFoundError:
        abort(404, description=f"No se encontró index.html en {HTML_DIR}")

app.register_blueprint(project_blueprint)
# ====================== ARCHIVOS ESTÁTICOS (Cesium, css, js, etc.) ======================
@app.route('/<path:filename>')
def serve_static(filename):
    """Sirve todos los archivos estáticos de tu carpeta server/"""
    # Importante: NO capturar rutas que empiecen con 'project/'
    if filename.startswith('project/'):
        abort(404)
    
    try:
        return send_from_directory(str(HTML_DIR), filename)
    except FileNotFoundError:
        abort(404)


# ====================== INICIO DE LA APLICACIÓN ======================

def run_webview():
    api=Api()
    window = webview.create_window(
        title="Cesium Fantasy",
        url=app,
        width=1000,
        height=700,
        resizable=True,
        js_api=api,
        min_size=(800, 600)
    )
    webview.start(debug=True)


if __name__ == "__main__":
    multiprocessing.freeze_support()

    print("Iniciando Cesium Fantasy...")

    p = multiprocessing.Process(
        target=run_webview,
        name="PyWebView_Process",
        daemon=False
    )

    p.start()
    print(f"Ventana iniciada en proceso PID: {p.pid}")

    try:
        while p.is_alive():
            time.sleep(5)
    except KeyboardInterrupt:
        print("Cerrando todo...")
        if p.is_alive():
            p.terminate()
            p.join()

    print("Programa terminado.")