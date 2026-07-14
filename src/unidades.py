#Carpeta de unidades
#Conversiones para valores de longitud, area y volumen

factor = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1,
    "km": 1000,
    "in": 0.0254
}

#Funcion de interfaz con usuario para pedir unidades

def pedir_unidad(mensaje):
    while True:
        unidad = input(mensaje).strip().lower() #muestra mensaje y lo guarda, quita espacios sobrantes, convierte todo en minuscula, para evitar bugs
        if unidad in factor:
            return unidad
        print("Unindad no valida, las opciones disponibles son mm, cm, m, km\n")

def convertir_longitud(valor, unidad_orig, unidad_reslt):
    valor_mt = valor * factor[unidad_orig]
    return valor_mt / factor[unidad_reslt]

def convertir_area(valor, unidad_orig, unidad_reslt):
    fact = (factor[unidad_orig] / factor[unidad_reslt])**2
    return valor*fact

def convertir_vol(valor, unidad_orig, unidad_reslt):
    fact = (factor[unidad_orig]/factor[unidad_reslt])**3
    return valor*fact
