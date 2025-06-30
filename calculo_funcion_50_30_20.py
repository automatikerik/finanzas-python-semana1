def calcular_50_30_20 (ingreso):
    necesidades = ingreso * 0.50
    deseos = ingreso * 0.30
    ahorro = ingreso * 0.20

    print("\nDistribucion 50-30-20")
    print(f"Necesidades: ${necesidades:.2f}")
    print(f"Deseos: ${deseos:.2f}")
    print(f"Ahorro: ${ahorro:.2f}")

    print("\nAnalisis de Ingreso:")
    if ingreso < 1000:
        print("Mejora ingreso de efectivo.")
    elif ingreso <= 3000:
        print("Ingreso aceptable pero se puede mejorar")
    elif ingreso <= 5000:
        print("Buen ingreso.")
    else:
        print("Excelente ingreso")

ingreso = float(input("¿Cuanto cobraste esta semana? "))
calcular_50_30_20(ingreso)