from flask import Blueprint,render_template

routes_base = Blueprint('routes_base', __name__, template_folder='templates')


@routes_base.route("/")
def home():
    return render_template("index.html")