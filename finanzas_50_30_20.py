ingreso = float(input("¿Cuanto cobraste esta semana? "))

necesidades = ingreso * 0.50
deseos = ingreso * 0.30
ahorro = ingreso * 0.20

print("\nDistribucion 50-30-20")
print(f"Necesidades: ${necesidades:.2f}")
print(f"Deseos: ${deseos:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
