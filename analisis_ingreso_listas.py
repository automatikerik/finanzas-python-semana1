ingresos = [1100, 1600, 1600, 1600]

def analisis_semanal(ingresos):
    total = 0
    promedio = 0
    for ingreso in ingresos:
        total += ingreso
    promedio = total / len(ingresos)
     
    print(f"Total ganado: ${total}")
    print(f"Promedio: ${promedio:.2f}")
    
    if promedio > 3000:
        print("Vas bien")
    elif promedio < 1500:
        print("Hay que mejorar los ingresos.")
    else:
        print("Ingreso aceptable")

print("Analisis Semanal.")
analisis_semanal(ingresos)
