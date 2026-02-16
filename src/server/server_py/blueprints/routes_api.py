from flask import Blueprint,request,jsonify

routes_api = Blueprint('routes_api', __name__, template_folder='templates')


@routes_api.route("/api/mouse/click",methods=['POST'])
def mouse_click():
    data = request.get_json()
    print(data)
    if not data:
        return jsonify({"error":'falta las coordenadas'}),400
    else:
        return jsonify({"sucses":'nada malo'}),200