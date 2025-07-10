#utils.py
import json

def cargar_ventas():
    try:
        with open("ventas.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}
    
def guardar_ventas(ventas):
    with open("ventas.json", "w") as archivo:
        json.dump(ventas, archivo, indent=4)
        
def resumen_ventas(ventas):
    total_general = 0
    
    with open ("ventas_resumen.txt", "w") as archivo:
        archivo.write("Resumen de ventas.\n")
        
        for producto, info in ventas.items():
            total = info["precio"] * info["cantidad"]
            total_general += total
            categoria = info.get("categoria", "sin categoria")
            linea = f"{producto}({categoria}): vendiste {info['cantidad']} piezas, ingreso total: ${total:.1f}\n"
            print(linea.strip())
            archivo.write(linea)
        
        archivo.write(f"Total general: ${total_general:.1f}\n")
        print(f"El total general es: ${total_general:.1f}")
        print("Resumen guardado en ventas_resumen.txt")
        
def categorias_productos(ventas):
    categoria_busqueda = input("Ingresa la categoria: ")
    encontrados = False
    print(f"\nProductos en la categoria '{categoria_busqueda}':")
    
    for producto, info in ventas.items():
        categoria = info.get("categoria", "Sin categoria")
        if categoria.lower() == categoria_busqueda.lower():
            total = info["precio"] * info["cantidad"]
            print(f"{producto}:{info['cantidad']} piezas, total: ${total:.1f}")
            encontrados = True
            
    if not encontrados:
        print("No se encontraron productos en esta categoria.")
        
def eliminar_producto(ventas):
    eliminado = input("Producto que desea eliminar: ")
    if eliminado in ventas:
        del ventas[eliminado]
        guardar_ventas(ventas)
        print("\nProducto eliminado.")
    else:
        print("Producto no encontrado.")
