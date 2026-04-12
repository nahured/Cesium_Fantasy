from flask import Blueprint,send_from_directory,abort
import webview

project_blueprint = Blueprint("project",__name__,url_prefix="/project")


@project_blueprint.route("/project/<path>")
def load_project(path):
    print("hola")