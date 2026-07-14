#Calculadora de propiedades geometricas de solidos

from figuras import calcular_cubo, calcular_esfera, calcular_cilindro, calcular_piramide
from unidades import pedir_unidad, convertir_longitud, convertir_area, convertir_vol
from resultados import guardar_resultados
from materiales import pedir_material

#Bienvenida al usuario
print("Bienvenidos! Esto es una calculadora para obtener distintas propiedades geomtricas de un solido, por favor, siga las indicaciones\n")

def menu():
    while True:
        print("Indique el solido con el que quiere trabajar: ")
        print("1. Cubo")
        print("2. Esfera")
        print("3. Cilindro")
        print("4. Piramide")
        print("5. Salir")

        entrada = input("Ingrese un numero: ")
        if not entrada.isdigit():
            print("Por favor, ingrese solo numeros del 1 al 5\n")
            continue
        solido = int(entrada)

        if solido not in [1, 2, 3, 4, 5]:
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
            lado = float(input("Ingrese la longitud del lado: "))
            lado_m = convertir_longitud(lado, u_entrada, "m")

            material, densidad = pedir_material()


            u_salida = pedir_unidad("Ingrese la unidad en la que quiere los resultados (cm, mm, km, in, m)")

            a_m2, v_m3, formulas= calcular_cubo(lado_m)
            area = convertir_area(a_m2, "m", u_salida)
            vol = convertir_vol(v_m3,"m", u_salida)

            masa = None
            if densidad:
                masa = densidad*v_m3

            print(f"\n{formulas["area"]}")
            print(f"Area: {area}{u_salida}^2")
            print(f"Volumen: {vol} {u_salida}^3")

            if masa:
                print(f"Masa: {masa} kg")

            rslt.append({
                "nombre": "Cubo", "area": area, "volumen": vol, "unidad": u_salida, "formulas": formulas, "material": material, "densidad": densidad, "masa": masa
            })

        
        #Formulas esfera
        elif op ==2:
            u_entrada = pedir_unidad("Ingrese la unidad en la que se encuentran sus medidas (cm, mm, km, in, m)")
            radio = float(input("Ingrese el radio: "))
            rm = convertir_longitud(radio, u_entrada, "m")

            material, densidad = pedir_material()
            u_salida = pedir_unidad("Ingrese la unidad en la que quiere los resultados (cm, mm, km, in, m)")

            a_m2, v_m3, formulas = calcular_esfera(rm)
            area = convertir_area(a_m2, "m", u_salida)
            vol = convertir_vol(v_m3, "m", u_salida)

            masa = None
            if densidad:
                masa = densidad*v_m3

            print(f"\n{formulas['area']}")
            print(f"Area: {area}{u_salida}^2")
            print(f"{formulas['volumen']}")
            print(f"Volumen: {vol} {u_salida}^3")

            if masa:
                print(f"Masa: {masa} kg")

            rslt.append({
                "nombre": "Esfera", "area": area, "volumen": vol, "unidad": u_salida, "formulas": formulas, "material": material, "densidad": densidad, "masa": masa
            })

            
        #cilindro
        elif op ==3:
            u_entrada = pedir_unidad("Ingrese la unidad en la que se encuentran sus medidas (cm, mm, km, in, m)")
            radio = float(input("Ingrese el radio: "))
            rm = convertir_longitud(radio, u_entrada, "m")
            altura = float(input("Ingrese la altura: "))
            hm = convertir_longitud(altura, u_entrada, "m")

            material, densidad = pedir_material()
            u_salida = pedir_unidad("Ingrese la unidad en la que quiere los resultados (cm, mm, km, in, m)")

            a_m2, v_m3, formulas = calcular_cilindro(rm, hm)
            area = convertir_area(a_m2, "m", u_salida)
            vol = convertir_vol(v_m3, "m", u_salida)

            masa = None
            if densidad:
                masa = densidad*v_m3

            print(f"\n{formulas['area']}")
            print(f"Area: {area}{u_salida}^2")
            print(f"{formulas['volumen']}")
            print(f"Volumen: {vol} {u_salida}^3")

            if masa:
                print(f"Masa: {masa} kg")

            rslt.append({
                "nombre": "Cilindro", "area": area, "volumen": vol, "unidad": u_salida, "formulas": formulas, "material": material, "densidad": densidad, "masa": masa
            })


        #piramide
        elif op ==4:
            u_entrada = pedir_unidad("Ingrese la unidad en la que se encuentran sus medidas (cm, mm, km, in, m)")
            l_base = float(input("Ingrese el lado de la base: "))
            lbm = convertir_longitud(l_base, u_entrada, "m")
            altura = float(input("Ingrese la altura de la piramide: "))
            hm = convertir_longitud(altura, u_entrada, "m")
            apotema = float(input("Ingrese la apotema (altura de cara lateral): "))
            am = convertir_longitud(apotema, u_entrada, "m")

            material, densidad = pedir_material()
            u_salida = pedir_unidad("Ingrese la unidad en la que quiere los resultados (cm, mm, km, in, m)")

            a_m2, v_m3, formulas = calcular_piramide(rm)
            area = convertir_area(a_m2, "m", u_salida)
            vol = convertir_vol(v_m3, "m", u_salida)

            masa = None
            if densidad:
                masa = densidad*v_m3

            print(f"\n{formulas['area']}")
            print(f"Area: {area}{u_salida}^2")
            print(f"{formulas['volumen']}")
            print(f"Volumen: {vol} {u_salida}^3")

            if masa:
                print(f"Masa: {masa} kg")

            rslt.append({
                "nombre": "Piramide", "area": area, "volumen": vol, "unidad": u_salida, "formulas": formulas, "material": material, "densidad": densidad, "masa": masa
            })
                  

    if rslt:
        nombre_archivo = input("Si desea guardar los resultados en un archivo txt, esscriba el nombre o presione Enter para salir")
        if nombre_archivo:
            if not nombre_archivo.endswith(".txt"):
                nombre_archivo += ".txt"
            guardar_resultados(rslt, nombre_archivo)
            print(f"Resultados guardador en: {nombre_archivo}")
        else:
            print("No se guardo ningun archivo")

    print("Gracias por utilizar la calculadora")

if __name__ == "__main__":
    main()
