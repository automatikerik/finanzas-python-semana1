ventas = {}

for i in range(3):
    nombre = input(f"Ingresa nombre del producto {i+1}: ")
    precio = float(input("Ingresa el precio del producto: $"))
    cantidad = int(input("Ingresa la cantidad del producto: "))
    
    ventas[nombre] = {"precio":precio, "cantidad":cantidad}
    
print("\nResumen de ventas.")
for producto, info in ventas.items():
    total = info["precio"] * info["cantidad"]
    print(f"{producto}: vendiste {info['cantidad']} piezas, ingreso total: ${total:.2f}")