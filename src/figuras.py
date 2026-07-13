#Carpeta de figuras geometricas
#Funciones para calcular area y volumen de solidos

def calcular_cubo(lado):
    area = 6*(lado**2)
    volumen=lado**3

    formulas = {
        "area": "Area = 6 * lado^2",
        "volumen": "Volumen = lado^3"
    }
    return area, volumen, formulas