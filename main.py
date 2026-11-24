
from funciones import (
    crear_tabla,
    registrar_producto,
    visualizar_productos,
    buscar_producto,
    actualizar_producto,
    eliminar_producto,
    reporte_stock_bajo
)


# Crear la tabla al iniciar el programa
crear_tabla()


# Menu principal
while True:

    print("\nSISTEMA DE GESTION DE INVENTARIO")
    print("1. Registrar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto por ID")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Reporte de stock bajo")
    print("7. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        registrar_producto()

    elif opcion == "2":
        visualizar_productos()

    elif opcion == "3":
        numero_texto = input("Ingrese el ID del producto que desea buscar: ")

        if numero_texto == "":
            print("Error: debe ingresar un ID.")
            continue

        numero_valido = True

        for caracter in numero_texto:
            if caracter < "0" or caracter > "9":
                numero_valido = False

        if numero_valido == False:
            print("Error: debe ingresar un numero entero.")

        else:
            id_producto = int(numero_texto)

            if id_producto <= 0:
                print("Error: el ID debe ser mayor que cero.")
            else:
                producto = buscar_producto(id_producto)

                if producto == None:
                    print("No se encontro el producto.")

                else:
                    print("\nPRODUCTO ENCONTRADO")
                    print("-------------------------")
                    print(f"ID: {producto[0]}")
                    print(f"Nombre: {producto[1]}")
                    print(f"Descripcion: {producto[2]}")
                    print(f"Cantidad: {producto[3]}")
                    print(f"Precio: ${producto[4]}")
                    print(f"Categoria: {producto[5]}")

    elif opcion == "4":
        numero_texto = input("Ingrese el ID del producto que desea actualizar: ")

        if numero_texto == "":
            print("Error: debe ingresar un ID.")
            continue

        numero_valido = True

        for caracter in numero_texto:
            if caracter < "0" or caracter > "9":
                numero_valido = False

        if numero_valido == False:
            print("Error: debe ingresar un numero entero.")

        else:
            id_producto = int(numero_texto)

            if id_producto <= 0:
                print("Error: el ID debe ser mayor que cero.")
            else:
                actualizar_producto(id_producto)

    elif opcion == "5":
        numero_texto = input("Ingrese el ID del producto que desea eliminar: ")

        if numero_texto == "":
            print("Error: debe ingresar un ID.")
            continue

        numero_valido = True

        for caracter in numero_texto:
            if caracter < "0" or caracter > "9":
                numero_valido = False

        if numero_valido == False:
            print("Error: debe ingresar un numero entero.")

        else:
            id_producto = int(numero_texto)

            if id_producto <= 0:
                print("Error: el ID debe ser mayor que cero.")
            else:
                eliminar_producto(id_producto)

    elif opcion == "6":
        limite_texto = input("Ingrese el limite de stock: ")

        if limite_texto == "":
            print("Error: debe ingresar un limite.")
            continue

        limite_valido = True

        for caracter in limite_texto:
            if caracter < "0" or caracter > "9":
                limite_valido = False

        if limite_valido == False:
            print("Error: debe ingresar un numero entero.")

        else:
            limite = int(limite_texto)
            reporte_stock_bajo(limite)

    elif opcion == "7":
        print("Programa finalizado.")
        break

    else:
        print("Opcion invalida. Seleccione una opcion del 1 al 7.")
