def menu():
    print("\nMENU")
    print("****")
    print("1. Agregar ingresos.")
    print("2. Ver promedio de ingresos.")
    print("3. Eliminar el ultimo ingreso.")
    print("4. Salir.")

def promedio_ingresos(ingresos):
    return sum(ingresos) / len(ingresos)

def eliminar_ultimo(ingresos):
    if ingresos:
        eliminado = ingresos.pop()
        print(f"Se elimino: ${eliminado}")
    else:
        print("La lista esta vacia.")
    
ingresos = []

while True:
    menu()
    opcion = int(input("¿Que opcion quieres realizar? "))
    if opcion == 1:
        ingreso = int(input("Ingreso que vas a agregar: $"))
        ingresos.append(ingreso)
    elif opcion == 2:
        if ingresos:
            prom = promedio_ingresos(ingresos)
            print("Tus ingresos actuales", ingresos)
            print(f"Tu promedio es: ${prom:.1f}")
        else:
            print("No hay ingresos aun.")
    elif opcion == 3:
        eliminar_ultimo(ingresos)
        print("Lista actuaizada:", ingresos)
    elif opcion == 4:
        print("Hasta luego.")
        break
    else:
        print("Opcion invalida.")
