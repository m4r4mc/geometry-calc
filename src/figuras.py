#Carpeta de figuras geometricas
#Funciones para calcular area y volumen de solidos
import numpy as np

def calcular_cubo(lado):
    area = np.multiply(6, np.power(lado, 2))
    volumen=np.power(lado, 3)

    formulas = {
        "area": "Area = 6 * lado^2",
        "volumen": "Volumen = lado^3"
    }
    return area, volumen, formulas

def calcular_esfera(radio):
    area = np.multiply(4*np.pi, np.power(radio, 2))
    volumen = np.multiply(4/3 * np.pi, np.power(radio, 3))
    formulas = {
        "area": "Area = 4*pi*r^2",
        "volumen": "Volumen = (4/3)*pi*r^3"
    }
    return area, volumen, formulas

def calcular_cilindro(radio, altura):
    area = np.multiply(2*np.pi*radio, (radio+altura))
    volumen = np.multiply(np.pi*np.power(radio, 2), altura)
    formulas = {
        "area": "Area = 2*pi*r*(r + h)",
        "volumen": "Volumen = pi*r^2 *h"
    }
    return area, volumen, formulas

def calcular_piramide(l_base, altura, apotema):
    area = np.add(np.power(l_base,2), np.multiply(2*l_base, apotema))
    volumen = np.divide(np.multiply(np.power(l_base, 2), altura), 3)
    formulas = {
        "area": "Area = l^2 +2l*a, l = lado base",
        "volumen": "Volumen = (l^2 * a)/3"
    }
    return area, volumen, formulas

