#Calculadora de propiedades geometricas de solidos

from figuras import calcular_cubo
from unidades import pedir_unidad, convertir_longitud, convertir_area, convertir_vol
from resultados import guardar_resultados

#Bienvenida al usuario
print("Bienvenidos! Esto es una calculadora para obtener distintas propiedades geomtricas de un solido, por favor, siga las indicaciones")

def menu():
    while True:
        print("Indique el solido con el que quiere trabajar: ")
        print("1. Cubo")
        print("2. Esfera")
        print("3. Cilindro")
        print("4. Piramide")
        print("5. Salir")

        solido = input("Ingrese un numero: ")
        if not solido.isdigit() or solido not in [1, 2, 3, 4,5]:
            print("Por favor, ingrese solo numeros del 1 al 5\n")
            continue
        return solido
    
def main():
    rslt = []


    while True:
        op = menu()

        if op == 5:
            print("Gracias por utilizar la calculadora")
            break

        #cubo
        elif op == 1:
            u_entrada = pedir_unidad("Ingrese la unidad en la que se encuentran sus medidas (cm, mm, km, in, m)")
            u_salida = pedir_unidad("Ingrese la unidad en la que quiere los resultados (cm, mm, km, in, m)")

            lado = float(input("Ingrese la longitud del lado: "))

