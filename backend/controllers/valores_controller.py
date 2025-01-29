from flask import jsonify, request
from models.valores_model import ValoresModel, TiposModel

def obtener_valores():
    valores = ValoresModel.obtener_todos()
    return jsonify(valores)

def obtener_valor(id):
    valor = ValoresModel.obtener_por_id(id)
    return jsonify(valor) if valor else ('', 404)

def agregar_valor():
    data = request.json
    ValoresModel.agregar(data['tipo_id'], data['fecha'], data['valor'])
    return jsonify({'mensaje': 'Valor agregado'}), 201

def actualizar_valor(id):
    data = request.json
    ValoresModel.actualizar(id, data['tipo_id'], data['fecha'], data['valor'])
    return jsonify({'mensaje': 'Valor actualizado'})

def desactivar_valor(id):
    ValoresModel.desactivar(id)
    return jsonify({'mensaje': 'Valor desactivado'})

def obtener_tipos():
    tipos = TiposModel.obtener_todos()  # Usamos el método del modelo para obtener los tipos
    return jsonify(tipos)  # Devolvemos los tipos en formato JSON
