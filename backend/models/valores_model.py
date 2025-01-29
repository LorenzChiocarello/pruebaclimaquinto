from utils.db import mysql

class ValoresModel:
    @staticmethod
    def obtener_todos():
        cursor = mysql.connection.cursor()
        cursor.execute("""
            SELECT v.id, v.tipo_id, t.tipo AS tipo, v.fecha, v.valor, v.status
            FROM valores v
            JOIN tipos t ON v.tipo_id = t.id
            WHERE v.status = 'activo'
        """)
        datos = cursor.fetchall()
        cursor.close()
        return datos
    
    @staticmethod
    def obtener_por_id(id):
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM valores WHERE id = %s", (id,))
        dato = cursor.fetchone()
        cursor.close()
        return dato
    
    @staticmethod
    def agregar(tipo_id, fecha, valor):
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO valores (tipo_id, fecha, valor, status) VALUES (%s, %s, %s, 'activo')", (tipo_id, fecha, valor))
        mysql.connection.commit()
        cursor.close()
        return True
    
    @staticmethod
    def actualizar(id, tipo_id, fecha, valor):
        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE valores SET tipo_id = %s, fecha = %s, valor = %s WHERE id = %s", (tipo_id, fecha, valor, id))
        mysql.connection.commit()
        cursor.close()
        return True
    
    @staticmethod
    def desactivar(id):
        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE valores SET status = 'inactivo' WHERE id = %s", (id,))
        mysql.connection.commit()
        cursor.close()
        return True
    
class TiposModel:
    @staticmethod
    def obtener_todos():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT id, tipo FROM tipos")  # Suponiendo que hay una tabla 'tipos' con 'id' y 'nombre'
        datos = cursor.fetchall()
        cursor.close()
        return datos


