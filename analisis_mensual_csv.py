def generar_csv(historial):
    with open("reporte_mensual.csv", "w") as archivo:
        
        archivo.write("Semana, Ingreso1, Ingreso2, Ingreso3, Promedio\n")
        for i, semana in enumerate(historial):
            promedio = sum(semana) / len(semana)
        
            fila = f"{i+1}," + ",".join(str(monto) for monto in semana) + f",{promedio:.2f}\n"
            archivo.write(fila)
        
historial = [[1200, 1300, 1500], [1400, 1600, 1800], [1100, 900, 950], [1700, 1600, 1650]]

generar_csv(historial)
print("Archivo reporte mensual generado.")
