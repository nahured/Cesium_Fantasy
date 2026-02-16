from flask import Flask, render_template
from src.server.server_py.blueprints.routes_base import routes_base
from src.server.server_py.blueprints.routes_api import routes_api
import logging

def loggin():
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)

loggin()

def run_server():
    app = Flask(__name__)
    app.register_blueprint(routes_base)
    app.register_blueprint(routes_api)
    app.run(
        debug = False,
        use_reloader = False,
        host = "0.0.0.0",
        port=6969,
        threaded=True,
    )