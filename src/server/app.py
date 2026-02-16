from flask import Flask, render_template
from src.server.server_py.blueprints.routes_base import routes_base
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

def run_server():
    app = Flask(__name__)
    app.register_blueprint(routes_base)
    app.run(
        debug = False,
        use_reloader = False,
        host = "0.0.0.0",
        port=6969,
        threaded=True,
    )