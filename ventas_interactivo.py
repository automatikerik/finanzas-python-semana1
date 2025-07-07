ventas = {}

while True:
    print("\nMenu")
    print("1. Agregar producto.")
    print("2. Ver resumen.")
    print("3. Eliminar producto")
    print("4. Salir")
    
    opcion = int(input("Opcion: "))
    
    if opcion == 1:
        for i in range(1):
            nombre = input("Ingresa nombre del producto: ")
            precio = float(input("Ingresa el precio del producto: $"))
            cantidad = int(input("Ingresa la cantidad del producto: "))
            print("Producto agregado.")
    
            ventas[nombre] = {"precio":precio, "cantidad":cantidad}
    elif opcion == 2:
        print("\nResumen de ventas.")
        total_general = 0
        
        with open ("ventas_resumen.txt", "w") as archivo:
            archivo.write("Resumen de ventas.\n")
            
            for producto, info in ventas.items():
                total = info["precio"] * info["cantidad"]
                total_general += total
                linea = f"{producto}: vendiste {info['cantidad']} piezas, ingreso total: ${total:.1f}\n"
                print(linea.strip())
                archivo.write(linea)
            
            archivo.write(f"Total general: ${total_general:.1f}\n")
            print(f"El total general es: ${total_general:.1f}")
            print("Resumen guardado en ventas_resumen.txt")
    elif opcion == 3:
        eliminado = input("Producto que desea eliminar: ")
        if eliminado in ventas:
            del ventas[eliminado]
            print("\nProducto eliminado.")
        else:
            print("Producto no encontrado.")
    elif opcion == 4:
        print("Hasta luego.")
        break
    else:
        print("Opcion invalida, intente de nuevo.")