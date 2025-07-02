def ingreso_semanal():
    ingresos = []
    for i in range(3):
        monto = int(input("Ingresa el monto: $"))
        ingresos.append(monto)
    return ingresos

def mostrar_historial(historial):
    for i, semana in enumerate(historial):
        prom = sum(semana) / len(semana)
        print(f"Semana {i+1} ingresos = {semana} y promedio = {prom:.1f}")
        pass
        
def guardar_en_archivo(historial):
    with open("historial.txt", "w") as archivo:
        for i, semana in enumerate(historial):
            prom = sum(semana) / len(semana)
            linea = f"Semana {i+1} ingresos = {semana} y promedio = {prom:.1f}\n"
            archivo.write(linea)
            pass
        
def cargar_historial():
    try:
        with open ("historial.txt", "r") as archivo:
            print("Historial cargado desde archivo.")
            for linea in archivo:
                print(linea.strip())
    except FileNotFoundError:
        print("No se encontro ningun historial guardado")

historial = []
cargar_historial()

while True:
    print("\nMENU")
    print("****")
    print("1. Agregar ingresos.")
    print("2. Ver historial completo")
    print("3. Guardar historial en archivo.")
    print("4. Salir")
    
    opcion = int(input("Ingresa una opcion: "))
    
    if opcion == 1:
        semana = ingreso_semanal()
        historial.append(semana)
    elif opcion == 2:
        mostrar_historial(historial)
    elif opcion == 3:
        guardar_en_archivo(historial)
    elif opcion == 4:
        print("Hasta luego.")
        break
    else:
        print("Opcion invalida.")

