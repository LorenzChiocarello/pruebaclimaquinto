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
    tipos = TiposModel.obtener_todos()  
    return jsonify(tipos)  

"""from flask import jsonify, request
from app.models.valores_model import ValoresModel, TiposModel

def obtener_valores():
    try:
        valores = ValoresModel.obtener_todos()
        return jsonify(valores)
    except Exception as e:
        return jsonify({'error': 'Error al obtener valores'}), 500

def obtener_valor(id):
    try:
        valor = ValoresModel.obtener_por_id(id)
        if valor:
            return jsonify(valor)
        return jsonify({'error': 'Valor no encontrado'}), 404
    except Exception as e:
        return jsonify({'error': 'Error al obtener el valor'}), 500

def agregar_valor():
    try:
        data = request.json
        if not all(key in data for key in ['tipo_id', 'fecha', 'valor']):
            return jsonify({'error': 'Faltan campos requeridos'}), 400
        
        success = ValoresModel.agregar(
            data['tipo_id'],
            data['fecha'],
            data['valor']
        )
        
        if success:
            return jsonify({'mensaje': 'Valor agregado correctamente'}), 201
        return jsonify({'error': 'Error al agregar valor'}), 400
    except Exception as e:
        return jsonify({'error': 'Error en el servidor'}), 500

def actualizar_valor(id):
    try:
        data = request.json
        if not all(key in data for key in ['tipo_id', 'fecha', 'valor']):
            return jsonify({'error': 'Faltan campos requeridos'}), 400
        
        success = ValoresModel.actualizar(
            id,
            data['tipo_id'],
            data['fecha'],
            data['valor']
        )
        
        if success:
            return jsonify({'mensaje': 'Valor actualizado correctamente'})
        return jsonify({'error': 'Error al actualizar valor'}), 400
    except Exception as e:
        return jsonify({'error': 'Error en el servidor'}), 500

def desactivar_valor(id):
    try:
        success = ValoresModel.desactivar(id)
        if success:
            return jsonify({'mensaje': 'Valor desactivado correctamente'})
        return jsonify({'error': 'Error al desactivar valor'}), 400
    except Exception as e:
        return jsonify({'error': 'Error en el servidor'}), 500

def obtener_tipos():
    try:
        tipos = TiposModel.obtener_todos()
        return jsonify(tipos)
    except Exception as e:
        return jsonify({'error': 'Error al obtener tipos'}), 500"""