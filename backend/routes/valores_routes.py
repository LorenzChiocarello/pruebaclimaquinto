from flask import Blueprint
from controllers.valores_controller import obtener_valores, obtener_valor, agregar_valor, actualizar_valor, desactivar_valor, obtener_tipos

valores_bp = Blueprint('valores', __name__)

valores_bp.route('/valores', methods=['GET'])(obtener_valores)
valores_bp.route('/valores/<int:id>', methods=['GET'])(obtener_valor)
valores_bp.route('/valores', methods=['POST'])(agregar_valor)
valores_bp.route('/valores/<int:id>', methods=['PUT'])(actualizar_valor)
valores_bp.route('/valores/<int:id>/desactivar', methods=['PUT'])(desactivar_valor)

valores_bp.route('/tipos', methods=['GET'])(obtener_tipos) 

