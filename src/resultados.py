#Modulo para guardar los resultados en un archivo de texto

def guardar_resultados(rslt, nom_archivo):
    with open(nom_archivo, "w") as archivo:
        archivo.write("RESULTADOS - CALCULADORA GEOMETRICA\n\n")

        contador = 1
        for i in rslt:
            archivo.write(f"Figura {contador}: {i['nombre']}\n")
            archivo.write("______________________________\n") #separar textos para que se vea mas ordenado
            archivo.write(f"{i['formulas']['area']}\n")
            archivo.write(f"Area: {i['area']} {i['unidad']}^2\n\n")
            archivo.write(f"{i['formulas']['volumen']}\n")
            archivo.write(f"Volumen: {i['volumen']} {i['unidad']}^3\n")

            if i["material"]:
                archivo.write(f"\n Material: {i['material']} \n")
                archivo.write(f"Densidad: {i['densidad']} kg/m^3 \n")
                archivo.write(f"Masa: {i['masa']} kg\n")
            
            archivo.write("\n______________________________\n\n")
            contador = contador +1


