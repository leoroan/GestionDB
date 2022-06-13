def insertar_cliente(nombre, apellido, telefono, domicilio):
    '''
        modulo para insertar un cliente a la bdd: recibe los datos y ejecuta .execeute
        requerido:
        - los parametros no pueden estar vacios, deben recibir por lo menos "sin informar" - a actualiziar
    '''
    import sqlite3
    import os
    
    try:
        con = sqlite3.connect(os.path.join(os.path.realpath("."),'configuration data','bdd','gestiondb.db'))
        cur = con.cursor()        
        orden = '''
            INSERT INTO table_clientes
            (nombre, apellido, telefono, domicilio)
            VALUES(?,?,?,?);
                '''
        datos = (nombre, apellido, telefono, domicilio)
        cur.execute(orden, datos)
        con.commit()
        cur.close()
        return True
    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if con:
          con.close()
          print("The SQLite connection is closed")

def insertar_vehiculo(patente, modelo, anio, chasis, motor, descrip):
    '''
        modulo para insertar un vehiculo a la bdd: recibe los datos y ejecuta .execeute
        requerido:
        - los parametros no pueden estar vacios, deben recibir por lo menos "sin informar" - a actualiziar
    '''
    import sqlite3
    import os

    try:
        con = sqlite3.connect(os.path.join(os.path.realpath("."),'configuration data','bdd','gestiondb.db'))
        cur = con.cursor()        
        orden = '''INSERT INTO table_vehiculos 
            (patente, modelo, anio, chasis, motor, descripcion)
            VALUES(?,?,?,?,?,?);'''
        datos = (patente, modelo, anio, chasis, motor, descrip)
        cur.execute(orden, datos)
        con.commit()
        cur.close()
        return True
    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if con:
          con.close()
          print("The SQLite connection is closed")

def insertar_orden(orden_numero, fecha, cant_horas, tercero_name, tercero_telefono, es_servicio):
    '''
        modulo para insertar una orden de trabajo a la bdd: recibe los datos y ejecuta .execeute
        requerido:
        - los parametros no pueden estar vacios, deben recibir por lo menos "sin informar" - a actualiziar
    '''
    import sqlite3
    import os

    try:
        con = sqlite3.connect('gestiondb.db')
        cur = con.cursor()        
        orden = '''INSERT INTO table_orden 
            (orden_numero, fecha, cant_horas, tercero_name, tercero_telefono, es_servicio)
            VALUES(?,?,?,?,?,?);'''
        datos = (orden_numero, fecha, cant_horas, tercero_name, tercero_telefono, es_servicio)
        cur.execute(orden, datos)
        con.commit()
        cur.close()
        return True
    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if con:
          con.close()
          print("The SQLite connection is closed")

def modificar_cliente(cliente_id, nombre, apellido, telefono, domicilio):
    '''
        Modulo para actualizar un cliente a partir de los datos por parametro
    '''
    import sqlite3
    import os

    try:
        con = sqlite3.connect('SQLite_Python.db')
        cur = con.cursor()
        sqlite_update_query = """
            UPDATE table_clientes
            SET nombre = ?, apellido = ?, telefono = ?, domicilio = ?
            WHERE cliente_id = ?
                              """
        data = (nombre, apellido, telefono, domicilio, cliente_id)
        cur.execute(sqlite_update_query, data)
        con.commit()
        print("Multiple columns updated successfully")
        con.commit()
        cur.close()
        return True
    except sqlite3.Error as error:
        print("Failed to update multiple columns of sqlite table", error)
    finally:
        if con:
          con.close()
          print("sqlite connection is closed")

def modificar_vehiculo(vehiculo_id, patente, modelo, anio, descripcion):
    '''
        Modulo para actualizar un vehiculo a partir de los datos por parametro
    '''
    import sqlite3
    import os

    try:
        con = sqlite3.connect('SQLite_Python.db')
        cur = con.cursor()
        sqlite_update_query = """
            UPDATE table_vehiculos
            SET patente = ?, modelo = ?, anio = ?, descripcion = ?
            WHERE vehiculo_id = ?
                              """
        data = (patente, modelo, anio, descripcion, vehiculo_id)
        cur.execute(sqlite_update_query, data)
        con.commit()
        print("Multiple columns updated successfully")
        con.commit()
        cur.close()
        return True
    except sqlite3.Error as error:
        print("Failed to update multiple columns of sqlite table", error)
    finally:
        if con:
          con.close()
          print("sqlite connection is closed")

def modificar_orden(orden_id, orden_numero, fecha, cant_horas, tercero_name, tercero_telefono, es_servicio):
    '''
        Modulo para actualizar una orden a partir de los datos por parametro
    '''
    import sqlite3
    import os

    try:
        con = sqlite3.connect('SQLite_Python.db')
        cur = con.cursor()
        sqlite_update_query = """
            UPDATE table_orden
            SET orden_numero = ?, fecha = ?, cant_horas = ?, tercero_name = ?, tercero_telefono = ?, es_servicio = ?
            WHERE orden_id = ?
                              """
        data = (orden_numero, fecha, cant_horas, tercero_name, tercero_telefono, es_servicio, orden_id)
        cur.execute(sqlite_update_query, data)
        con.commit()
        print("Multiple columns updated successfully")
        con.commit()
        cur.close()
        return True
    except sqlite3.Error as error:
        print("Failed to update multiple columns of sqlite table", error)
    finally:
        if con:
          con.close()
          print("sqlite connection is closed")
