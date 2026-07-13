#Modulo para guardar los resultados en un archivo de texto

def guardar_resultados(rslt, nom_archivo):
    with open(nom_archivo, "w") as archivo:
        archivo.write("RESULTADOS - CALCULADORA GEOMETRICA")

        for i in enumerate(rslt, start=1)
            archivo.write(f"Figura {i}: {r['nombre']}\n")
            archivo.write("________________________________") #separar textos para que se vea mas ordenado
            archivo.write(f"{r['formulas']['area']}\n")
            archivo.write(f"Area: {r['area']:.4f} {r['unidad']}^2\n\n")
            archivo.write(f"{r['formulas']['volumen']}\n")
            archivo.write(f"Volumen: {r['volumen']:.4f} {r['unidad']}^3\n")
        archivo.write("Gracias por usar la calculadora!")