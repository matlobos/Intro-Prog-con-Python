productos = []

while True:
    print("\\nSISTEMA DE GESTION DE PRODUCTOS")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        # Entrada de datos del producto
        nombre = input("Ingrese el nombre del producto: ")

        if nombre == "":
            print("Error: el nombre no puede estar vacio.")
            continue

        categoria = input("Ingrese la categoria del producto: ")

        if categoria == "":
            print("Error: la categoria no puede estar vacia.")
            continue

        precio_texto = input("Ingrese el precio entero, sin centavos: ")

        if precio_texto == "":
            print("Error: el precio no puede estar vacio.")
            continue

        # Validar que el precio contenga solamente numeros
        precio_valido = True

        for caracter in precio_texto:
            if caracter < "0" or caracter > "9":
                precio_valido = False

        if precio_valido == False:
            print("Error: debe ingresar un precio entero valido.")
            continue

        precio = int(precio_texto)

        if precio <= 0:
            print("Error: el precio debe ser mayor que cero.")
            continue

        # Guardar los datos en una sublista
        producto = [nombre, categoria, precio]
        productos.append(producto)

        print("Producto agregado correctamente.")

    elif opcion == "2":
        # Mostrar todos los productos registrados
        if len(productos) == 0:
            print("No hay productos registrados.")
        else:
            print("\\nPRODUCTOS REGISTRADOS")

            for i in range(len(productos)):
                print(f"{i + 1}. Nombre: {productos[i][0]}")
                print(f"   Categoria: {productos[i][1]}")
                print(f"   Precio: ${productos[i][2]}")

    elif opcion == "3":
        # Buscar productos por nombre
        nombre_buscar = input("Ingrese el nombre del producto que desea buscar: ")

        if nombre_buscar == "":
            print("Error: debe ingresar un nombre para buscar.")
            continue

        encontrados = 0

        for i in range(len(productos)):
            if nombre_buscar.lower() in productos[i][0].lower():
                print(f"Nombre: {productos[i][0]}")
                print(f"Categoria: {productos[i][1]}")
                print(f"Precio: ${productos[i][2]}")
                print("-------------------------")
                encontrados = encontrados + 1

        if encontrados == 0:
            print("No se encontraron productos.")

    elif opcion == "4":
        # Eliminar un producto por su numero en la lista
        if len(productos) == 0:
            print("No hay productos para eliminar.")
        else:
            print("\\nPRODUCTOS REGISTRADOS")

            for i in range(len(productos)):
                print(f"{i + 1}. {productos[i][0]}")

            numero_texto = input("Ingrese el numero del producto que desea eliminar: ")

            if numero_texto == "":
                print("Error: debe ingresar un numero.")
                continue

            numero_valido = True

            for caracter in numero_texto:
                if caracter < "0" or caracter > "9":
                    numero_valido = False

            if numero_valido == False:
                print("Error: debe ingresar un numero entero.")
                continue

            posicion = int(numero_texto)

            if posicion < 1 or posicion > len(productos):
                print("Error: el numero no corresponde a un producto.")
            else:
                producto_eliminar = productos[posicion - 1]
                productos.remove(producto_eliminar)
                print("Producto eliminado correctamente.")

    elif opcion == "5":
        print("Programa finalizado.")
        break

    else:
        print("Opcion invalida. Seleccione una opcion del 1 al 5.")