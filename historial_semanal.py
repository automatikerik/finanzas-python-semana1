def ingresar_semana():
    ingresos = []
    for i in range(3):
        monto = int(input("Ingresa el monto: $"))
        ingresos.append(monto)
    return ingresos

historial = []

while True:
    print("\nMENU")
    print("****")
    print("1. Agregar ingresos.")
    print("2. Ver historial completo")
    print("3. Salir.")
    
    opcion = int(input("¿Que opcion quieres realizar? "))
    
    if opcion == 1:
        semana = ingresar_semana()
        historial.append(semana)
        print("Ingresos registrados.")
    elif opcion == 2:
        for i, semana in enumerate(historial):
            prom = sum(semana) / len(semana)
            print(f"Semana {i+1}: ingresos = {semana}, promedio: {prom:.2f}")
    elif opcion == 3:
        print("Hasta luego.")
        break
    else:
        print("Opcion no valida. Intente de nuevo")
