from flask import Blueprint,request,jsonify
from pubsub import pub

routes_api = Blueprint('routes_api', __name__, template_folder='templates')


@routes_api.route("/api/mouse/click",methods=['POST'])
def mouse_click():
    data = request.get_json()
    if not data:
        return jsonify({"error":'falta las coordenadas'}),400
    else:
        if data["data"] == "None":
            pass
        else:
            pub.sendMessage('mouse_click_signal',data=data)
        return jsonify({"sucses":'nada malo'}),200