def ingresar_ingresos():
    ingresos = []
    for i in range (3):
        ingreso = int(input(f"Escribir ingreso {i+1}: $"))
        ingresos.append(ingreso)
    return ingresos

def promedio_ingresos(ingresos):
    return sum(ingresos) / len(ingresos)

def eliminar_ultimo(ingresos):
    if ingresos:
        eliminado = ingresos.pop()
        print(f"Se elimino: ${eliminado}")
    else:
        print("La lista esta vacia.")
        
ingreso = ingresar_ingresos()
print("\nMENU")
print("****")
print("1. Ver promedio de ingresos.")
print("2. Eliminar el ultimo ingreso.\n")
opcion = int(input("¿Cual opcion desea realizar? "))

if opcion == 1:
    prom = promedio_ingresos(ingreso)
    print("Tus ingresos actuales", ingreso)
    print(f"Tu promedio es: ${prom:.1f}")
elif opcion == 2:
    eliminar_ultimo(ingreso)
    print("Lista actuaizada:", ingreso)
else:
    print("Opcion no valida")
