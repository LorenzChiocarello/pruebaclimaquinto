from utils.db import mysql

class ValoresModel:

    def __init__(self, id=None, tipo_id=None, tipo=None, fecha=None, valor=None, status=None):
        self.id = id
        self.tipo_id = tipo_id
        self.tipo = tipo
        self.fecha = fecha
        self.valor = valor
        self.status = status
    
    @staticmethod
    def from_db_row(row):
        return ValoresModel(
            id=row[0],
            tipo_id=row[1],
            tipo=row[2],
            fecha=row[3],
            valor=row[4],
            status=row[5]
        )
    
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
        return [ValoresModel.from_db_row(row).__dict__ for row in datos]

    
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

    def __init__(self, id=None, tipo=None):
        self.id = id
        self.tipo = tipo
    
    @staticmethod
    def from_db_row(row):
        return TiposModel(
            id=row[0],
            tipo=row[1]
        )

    @staticmethod
    def obtener_todos():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT id, tipo FROM tipos")
        datos = cursor.fetchall()
        cursor.close()
        return [TiposModel.from_db_row(row).__dict__ for row in datos]

"""class ValoresModel:
    def __init__(self, id=None, tipo_id=None, tipo=None, fecha=None, valor=None, status=None):
        self.id = id
        self.tipo_id = tipo_id
        self.tipo = tipo
        self.fecha = fecha
        self.valor = valor
        self.status = status
    
    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_db_row(row):
        return ValoresModel(
            id=row[0],
            tipo_id=row[1],
            tipo=row[2],
            fecha=row[3],
            valor=row[4],
            status=row[5]
        ).__dict__
    
    @staticmethod
    def obtener_todos():
        cursor = mysql.connection.cursor()
        cursor.execute(SELECT v.id, v.tipo_id, t.tipo AS tipo, v.fecha, v.valor, v.status
            FROM valores v
            JOIN tipos t ON v.tipo_id = t.id
            WHERE v.status = 'activo')
        datos = cursor.fetchall()
        cursor.close()
        return [ValoresModel.from_db_row(row) for row in datos]

    @staticmethod
    def obtener_por_id(id):
        cursor = mysql.connection.cursor()
        cursor.execute
        dato = cursor.fetchone()
        cursor.close()
        return ValoresModel.from_db_row(dato) if dato else None
    
    @staticmethod
    def agregar(tipo_id, fecha, valor):
        try:
            cursor = mysql.connection.cursor()
            cursor.execute(
                "INSERT INTO valores (tipo_id, fecha, valor, status) VALUES (%s, %s, %s, 'activo')",
                (tipo_id, fecha, valor)
            )
            mysql.connection.commit()
            cursor.close()
            return True
        except Exception as e:
            mysql.connection.rollback()
            return False
    
    @staticmethod
    def actualizar(id, tipo_id, fecha, valor):
        try:
            cursor = mysql.connection.cursor()
            cursor.execute(
                "UPDATE valores SET tipo_id = %s, fecha = %s, valor = %s WHERE id = %s",
                (tipo_id, fecha, valor, id)
            )
            mysql.connection.commit()
            cursor.close()
            return True
        except Exception as e:
            mysql.connection.rollback()
            return False
    
    @staticmethod
    def desactivar(id):
        try:
            cursor = mysql.connection.cursor()
            cursor.execute(
                "UPDATE valores SET status = 'inactivo' WHERE id = %s",
                (id,)
            )
            mysql.connection.commit()
            cursor.close()
            return True
        except Exception as e:
            mysql.connection.rollback()
            return False

class TiposModel:
    def __init__(self, id=None, tipo=None):
        self.id = id
        self.tipo = tipo
    
    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_db_row(row):
        return TiposModel(
            id=row[0],
            tipo=row[1]
        ).__dict__

    @staticmethod
    def obtener_todos():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT id, tipo FROM tipos")
        datos = cursor.fetchall()
        cursor.close()
        return [TiposModel.from_db_row(row) for row in datos]"""

