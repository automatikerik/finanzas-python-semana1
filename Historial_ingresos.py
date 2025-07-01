ingresos = []

def agregar_ingreso(lista, monto): #Funcion para agregar a la lista
    lista.append(monto)
    return lista

agregar_ingreso(ingresos, int(input("Escribe tu primer ingreso: ")))
agregar_ingreso(ingresos, int(input("Escribe tu segundo ingreso: ")))
agregar_ingreso(ingresos, int(input("Escribe tu tercer ingrso: ")))

print("Ingresos:", ingresos)

def resumen(ingresos): #Funcion para mostrar total y promedio
    total = 0
    promedio = 0
    for ingreso in ingresos:
        total += ingreso
    promedio = total / len(ingresos)
    
    print(f"El total de tu ingreso es: ${total}")
    print(f"El promedio es: ${promedio:.1f}")
    
    if promedio > 2000:
            print("Es recomendable ahorrar.")
    else:
        print("Aun no es recomendable ahorrar.")

print("Resumen.")
resumen(ingresos)