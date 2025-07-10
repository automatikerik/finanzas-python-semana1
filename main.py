#main.py
from utils import cargar_ventas, guardar_ventas, resumen_ventas, categorias_productos, eliminar_producto

ventas = cargar_ventas()

while True:
    print("\nMenu")
    print("1. Agregar producto.")
    print("2. Ver resumen.")
    print("3. Ver productos por categoria.")
    print("4. Eliminar producto")
    print("5. Salir")
    
    opcion = int(input("Opcion: "))
    
    if opcion == 1:
        for i in range(1):
            nombre = input("Ingresa nombre del producto: ")
            categoria = input("Ingresa la categoria del producto: ")
            precio = float(input("Ingresa el precio del producto: $"))
            cantidad = int(input("Ingresa la cantidad del producto: "))
            print("Producto agregado.")
    
            ventas[nombre] = {"precio":precio, "cantidad":cantidad, "categoria":categoria}
            guardar_ventas(ventas)
            
    elif opcion == 2:
        resumen_ventas(ventas)
        
    elif opcion == 3:
        categorias_productos(ventas)
        
    elif opcion == 4:
        eliminar_producto(ventas)
    
    elif opcion == 5:
        print("Hasta luego.")
        break
    
    else:
        print("Opcion no valida")