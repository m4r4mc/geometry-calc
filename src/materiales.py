#Datos de materiales estandar (kg/m^3)
#Funcion para preguntar si tiene un materiales

densidades = {
    "hierro": 7874,
    "acero": 7850,
    "aluminio": 2700,
    "cobre": 8960,
    "oro": 19300,
    "plata": 10490,
    "vidrio": 2500,
    "madera": 600,
    "concreto": 2400,
    "plastico (pvc)": 1380
}

def pedir_material():
    while True:
        print("1. El solido tiene un material asociado")
        print("2. El solido NO tiene un material asociado")
        mat = int(input("Ingrese un numero con respecto al material del solido: "))

        if mat not in [1,2]:
            print("Ingrese solamente los numeros 1 o 2")
        else:
            break
        return mat
    if mat == 2:
        return None
    
    print("Materiales disponibles: ")
    materiales = list(densidades.keys())

    for i, nombre in enumerate(materiales, start=1): #imprimir lista de materiales
        print(f"{i}. {nombre}")

    while True:
        op = int(input("Ingrese un numero para elegir el material: "))
        if op in range(1, len(materiales)+1):
            nom = materiales[op -1]
            return nom, densidades[nombre]
        
        else:
            print("Ingrese solamente un numero valido")

            