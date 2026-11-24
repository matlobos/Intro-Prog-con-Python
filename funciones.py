
import sqlite3


def crear_tabla():
    """
    Crea la base de datos y la tabla de productos
    si todavía no existen.
    """

    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()

    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                descripcion TEXT,
                cantidad INTEGER NOT NULL,
                precio REAL NOT NULL,
                categoria TEXT
            )
        """)

        conexion.commit()
        print("Base de datos creada correctamente.")

    except sqlite3.Error as error:
        conexion.rollback()
        print("Error al crear la tabla:", error)

    finally:
        conexion.close()


def registrar_producto():
    """
    Solicita los datos de un producto y los guarda
    en la base de datos.
    """

    nombre = input("Ingrese el nombre del producto: ")

    if nombre == "":
        print("Error: el nombre no puede estar vacio.")
        return

    descripcion = input("Ingrese la descripcion del producto: ")

    cantidad_texto = input("Ingrese la cantidad disponible: ")

    if cantidad_texto == "":
        print("Error: la cantidad no puede estar vacia.")
        return

    # Validar que la cantidad contenga solamente numeros
    cantidad_valida = True

    for caracter in cantidad_texto:
        if caracter < "0" or caracter > "9":
            cantidad_valida = False

    if cantidad_valida == False:
        print("Error: debe ingresar una cantidad entera.")
        return

    cantidad = int(cantidad_texto)

    precio_texto = input("Ingrese el precio del producto: ")

    if precio_texto == "":
        print("Error: el precio no puede estar vacio.")
        return

    # Validar que el precio contenga numeros y un solo punto decimal
    precio_valido = True
    puntos = 0

    for caracter in precio_texto:
        if caracter == ".":
            puntos = puntos + 1
        elif caracter < "0" or caracter > "9":
            precio_valido = False

    if precio_valido == False or puntos > 1:
        print("Error: debe ingresar un precio valido.")
        return

    precio = float(precio_texto)

    if precio <= 0:
        print("Error: el precio debe ser mayor que cero.")
        return

    categoria = input("Ingrese la categoria del producto: ")

    if categoria == "":
        print("Error: la categoria no puede estar vacia.")
        return

    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()

    try:
        cursor.execute("""
            INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
            VALUES (?, ?, ?, ?, ?)
        """, (nombre, descripcion, cantidad, precio, categoria))

        conexion.commit()

        print("Producto registrado correctamente.")

    except sqlite3.Error as error:
        conexion.rollback()
        print("Error al registrar el producto:", error)

    finally:
        conexion.close()


def visualizar_productos():
    """
    Consulta y muestra todos los productos registrados
    en la base de datos.
    """

    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()

    try:
        cursor.execute("SELECT * FROM productos")

        productos = cursor.fetchall()

        if len(productos) == 0:
            print("No hay productos registrados.")

        else:
            print("\nPRODUCTOS REGISTRADOS")

            for producto in productos:
                print("-------------------------")
                print(f"ID: {producto[0]}")
                print(f"Nombre: {producto[1]}")
                print(f"Descripcion: {producto[2]}")
                print(f"Cantidad: {producto[3]}")
                print(f"Precio: ${producto[4]}")
                print(f"Categoria: {producto[5]}")

    except sqlite3.Error as error:
        print("Error al consultar los productos:", error)

    finally:
        conexion.close()


def buscar_producto(id_producto):
    """
    Busca un producto en la base de datos utilizando su ID.
    Retorna los datos del producto si existe.
    """

    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()

    try:
        cursor.execute(
            "SELECT * FROM productos WHERE id = ?",
            (id_producto,)
        )

        producto = cursor.fetchone()

        return producto

    except sqlite3.Error as error:
        print("Error al buscar el producto:", error)
        return None

    finally:
        conexion.close()


def actualizar_producto(id_producto):
    """
    Actualiza los datos de un producto mediante su ID.
    """

    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()

    try:
        cursor.execute(
            "SELECT * FROM productos WHERE id = ?",
            (id_producto,)
        )

        producto = cursor.fetchone()

        if producto == None:
            print("No se encontro el producto.")
            return

        print("\nPRODUCTO ACTUAL")
        print(f"Nombre: {producto[1]}")
        print(f"Descripcion: {producto[2]}")
        print(f"Cantidad: {producto[3]}")
        print(f"Precio: ${producto[4]}")
        print(f"Categoria: {producto[5]}")

        print("\nINGRESE LOS NUEVOS DATOS")

        nombre = input("Nuevo nombre: ")

        if nombre == "":
            print("Error: el nombre no puede estar vacio.")
            return

        descripcion = input("Nueva descripcion: ")

        cantidad_texto = input("Nueva cantidad: ")

        if cantidad_texto == "":
            print("Error: la cantidad no puede estar vacia.")
            return

        cantidad_valida = True

        for caracter in cantidad_texto:
            if caracter < "0" or caracter > "9":
                cantidad_valida = False

        if cantidad_valida == False:
            print("Error: debe ingresar una cantidad entera.")
            return

        cantidad = int(cantidad_texto)

        precio_texto = input("Nuevo precio: ")

        if precio_texto == "":
            print("Error: el precio no puede estar vacio.")
            return

        precio_valido = True
        puntos = 0

        for caracter in precio_texto:
            if caracter == ".":
                puntos = puntos + 1
            elif caracter < "0" or caracter > "9":
                precio_valido = False

        if precio_valido == False or puntos > 1:
            print("Error: debe ingresar un precio valido.")
            return

        precio = float(precio_texto)

        if precio <= 0:
            print("Error: el precio debe ser mayor que cero.")
            return

        categoria = input("Nueva categoria: ")

        if categoria == "":
            print("Error: la categoria no puede estar vacia.")
            return

        cursor.execute("""
            UPDATE productos
            SET nombre = ?, descripcion = ?, cantidad = ?,
                precio = ?, categoria = ?
            WHERE id = ?
        """, (nombre, descripcion, cantidad, precio, categoria, id_producto))

        conexion.commit()

        print("Producto actualizado correctamente.")

    except sqlite3.Error as error:
        conexion.rollback()
        print("Error al actualizar el producto:", error)

    finally:
        conexion.close()



def eliminar_producto(id_producto):
    """
    Elimina un producto de la base de datos mediante su ID.
    """

    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()

    try:
        cursor.execute(
            "SELECT * FROM productos WHERE id = ?",
            (id_producto,)
        )

        producto = cursor.fetchone()

        if producto == None:
            print("No se encontro el producto.")
            return

        print("\nPRODUCTO A ELIMINAR")
        print(f"ID: {producto[0]}")
        print(f"Nombre: {producto[1]}")
        print(f"Categoria: {producto[5]}")

        confirmacion = input("¿Esta seguro que desea eliminarlo? (S/N): ")

        if confirmacion.lower() == "s":

            cursor.execute(
                "DELETE FROM productos WHERE id = ?",
                (id_producto,)
            )

            conexion.commit()

            print("Producto eliminado correctamente.")

        else:
            print("Eliminacion cancelada.")

    except sqlite3.Error as error:
        conexion.rollback()
        print("Error al eliminar el producto:", error)

    finally:
        conexion.close()


def reporte_stock_bajo(limite):
    """
    Muestra los productos cuya cantidad disponible
    es igual o inferior al limite indicado.
    """

    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()

    try:
        cursor.execute(
            "SELECT * FROM productos WHERE cantidad <= ?",
            (limite,)
        )

        productos = cursor.fetchall()

        if len(productos) == 0:
            print("No hay productos con stock bajo.")

        else:
            print("\nREPORTE DE STOCK BAJO")

            for producto in productos:
                print("-------------------------")
                print(f"ID: {producto[0]}")
                print(f"Nombre: {producto[1]}")
                print(f"Descripcion: {producto[2]}")
                print(f"Cantidad: {producto[3]}")
                print(f"Precio: ${producto[4]}")
                print(f"Categoria: {producto[5]}")

    except sqlite3.Error as error:
        print("Error al generar el reporte:", error)

    finally:
        conexion.close()
