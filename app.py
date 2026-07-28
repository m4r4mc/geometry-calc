#Codigo de app en streamlit para facilitar visualización de datos brindados al usuario

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from itertools import product, combinations

st.set_page_config(
  page_title="Calculadora de propiedades de sólidos",
  page_icon="📐",
  layout="centered"
)

#constantes de materiales, kg/m^3
densidades={
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

#factor de conversiones
factor = {
  "mm": 0.001,
  "cm": 0.01,
  "m": 1,
  "km": 1000,
  "in": 0.0254
}

#Funciones figuras geometricas

def calcular_cubo(lado):
    area = np.multiply(6, np.power(lado, 2))
    volumen = np.power(lado, 3)
    formulas = {
        "area": "Area = 6 * lado^2",
        "volumen": "Volumen = lado^3"
    }
    return area, volumen, formulas


def calcular_esfera(radio):
    area = np.multiply(4 * np.pi, np.power(radio, 2))
    volumen = np.multiply(4 / 3 * np.pi, np.power(radio, 3))
    formulas = {
        "area": "Area = 4*pi*r^2",
        "volumen": "Volumen = (4/3)*pi*r^3"
    }
    return area, volumen, formulas


def calcular_cilindro(radio, altura):
    area = np.multiply(2 * np.pi * radio, (radio + altura))
    volumen = np.multiply(np.pi * np.power(radio, 2), altura)
    formulas = {
        "area": "Area = 2*pi*r*(r + h)",
        "volumen": "Volumen = pi*r^2 *h"
    }
    return area, volumen, formulas


def calcular_piramide(l_base, altura, apotema):
    area = np.add(np.power(l_base, 2), np.multiply(2 * l_base, apotema))
    volumen = np.divide(np.multiply(np.power(l_base, 2), altura), 3)
    formulas = {
        "area": "Area = l^2 + 2*l*a, l = lado base",
        "volumen": "Volumen = (l^2 * a)/3"
    }
    return area, volumen, formulas


#Funciones conversion de unidades
def convertir_longitud(valor, unidad_orig, unidad_reslt):
    valor_mt = valor * factor[unidad_orig]
    return valor_mt / factor[unidad_reslt]


def convertir_area(valor, unidad_orig, unidad_reslt):
    fact = (factor[unidad_orig] / factor[unidad_reslt]) ** 2
    return valor * fact


def convertir_vol(valor, unidad_orig, unidad_reslt):
    fact = (factor[unidad_orig] / factor[unidad_reslt]) ** 3
    return valor * fact


#solidos grafica (para app, no en py)
def graficar_cubo(lado):
    lado = lado if lado > 0 else 1
    fig = plt.figure(figsize=(4, 4))
    ax = fig.add_subplot(111, projection="3d")

    r = [0, lado]
    vertices = np.array(list(product(r, r, r)))
    for s, e in combinations(vertices, 2):
        if np.sum(np.abs(s - e)) == lado:
            ax.plot3D(*zip(s, e), color="steelblue", linewidth=2)

    ax.set_box_aspect([1, 1, 1])
    ax.set_axis_off()
    return fig


def graficar_esfera(radio):
    radio = radio if radio > 0 else 1
    fig = plt.figure(figsize=(4, 4))
    ax = fig.add_subplot(111, projection="3d")

    u = np.linspace(0, 2 * np.pi, 30)
    v = np.linspace(0, np.pi, 30)
    x = radio * np.outer(np.cos(u), np.sin(v))
    y = radio * np.outer(np.sin(u), np.sin(v))
    z = radio * np.outer(np.ones(np.size(u)), np.cos(v))

    ax.plot_wireframe(x, y, z, color="seagreen", linewidth=0.5)
    ax.set_box_aspect([1, 1, 1])
    ax.set_axis_off()
    return fig


def graficar_cilindro(radio, altura):
    radio = radio if radio > 0 else 1
    altura = altura if altura > 0 else 1
    fig = plt.figure(figsize=(4, 4))
    ax = fig.add_subplot(111, projection="3d")

    theta = np.linspace(0, 2 * np.pi, 30)

    #Superficie lateral
    z = np.linspace(0, altura, 2)
    theta_grid, z_grid = np.meshgrid(theta, z)
    x_grid = radio * np.cos(theta_grid)
    y_grid = radio * np.sin(theta_grid)
    ax.plot_wireframe(x_grid, y_grid, z_grid, color="darkorange", linewidth=0.6)

    #Tapa inferior y superior (circulos)
    x_circulo = radio * np.cos(theta)
    y_circulo = radio * np.sin(theta)
    ax.plot(x_circulo, y_circulo, 0, color="darkorange", linewidth=1)
    ax.plot(x_circulo, y_circulo, altura, color="darkorange", linewidth=1)

    ax.set_box_aspect([1, 1, max(altura / (2 * radio), 0.3)])
    ax.set_axis_off()
    return fig


def graficar_piramide(l_base, altura):
    l_base = l_base if l_base > 0 else 1
    altura = altura if altura > 0 else 1
    fig = plt.figure(figsize=(4, 4))
    ax = fig.add_subplot(111, projection="3d")

    mitad = l_base / 2
    base = np.array([
        [-mitad, -mitad, 0],
        [mitad, -mitad, 0],
        [mitad, mitad, 0],
        [-mitad, mitad, 0],
    ])
    apice = np.array([0, 0, altura])

    #Aristas de la base
    for i in range(4):
        s = base[i]
        e = base[(i + 1) % 4]
        ax.plot3D(*zip(s, e), color="crimson", linewidth=2)

    #Aristas laterales (de cada esquina de la base al apice)
    for v in base:
        ax.plot3D(*zip(v, apice), color="crimson", linewidth=2)

    ax.set_box_aspect([1, 1, 1])
    ax.set_axis_off()
    return fig

#reporte texto (descargar)
def generar_reporte(rslt):
    lineas = []
    lineas.append("Resultados calculadora propiedades geometricas de solidos\n")

    contador = 1
    for i in rslt:
        lineas.append(f"Figura {contador}: {i['nombre']}")
        lineas.append("______________________________")
        lineas.append(f"{i['formulas']['area']}")
        lineas.append(f"Area: {i['area']:.4f} {i['unidad']}^2\n")
        lineas.append(f"{i['formulas']['volumen']}")
        lineas.append(f"Volumen: {i['volumen']:.4f} {i['unidad']}^3")

        if i["material"]:
            lineas.append(f"\nMaterial: {i['material']}")
            lineas.append(f"Densidad: {i['densidad']} kg/m^3")
            lineas.append(f"Masa: {i['masa']:.4f} kg")

        lineas.append("\n______________________________\n")
        contador = contador + 1

    lineas.append("Gracias por usar la calculadora!")
    return "\n".join(lineas)


#Estado de sesion
if "rslt" not in st.session_state:
    st.session_state.rslt = []

#Interfaz
st.title("Calculadora de Propiedades Geometricas")
st.write(
    "Bienvenid@. Esta calculadora obtiene distintas propiedades geometricas "
    "de un solido. Elige una figura, ingresa sus medidas, y si aplica, "
    "un material para calcular tambien la masa."
)

st.divider()


#Seleccion de figuras
opciones_figuras = ["Cubo", "Esfera", "Cilindro", "Piramide"]
figura = st.selectbox("Selecciona la figura con la que quieres trabajar:", opciones_figuras)

unidades_disponibles = list(factor.keys())

col1, col2 = st.columns(2)
with col1:
    u_entrada = st.selectbox("Unidad de las medidas ingresadas:", unidades_disponibles, key="u_entrada")
with col2:
    u_salida = st.selectbox("Unidad deseada para los resultados:", unidades_disponibles, key="u_salida")

st.subheader("Medidas")

col_medidas, col_figura = st.columns([1, 1])


with col_medidas:
    if figura == "Cubo":
        lado = st.number_input("Longitud del lado:", min_value=0.0, step=0.1, format="%.4f")

    elif figura == "Esfera":
        radio = st.number_input("Radio:", min_value=0.0, step=0.1, format="%.4f")

    elif figura == "Cilindro":
        radio = st.number_input("Radio:", min_value=0.0, step=0.1, format="%.4f")
        altura = st.number_input("Altura:", min_value=0.0, step=0.1, format="%.4f")

    elif figura == "Piramide":
        l_base = st.number_input("Lado de la base:", min_value=0.0, step=0.1, format="%.4f")
        altura = st.number_input("Altura de la piramide:", min_value=0.0, step=0.1, format="%.4f")
        apotema = st.number_input("Apotema (altura de cara lateral):", min_value=0.0, step=0.1, format="%.4f")

with col_figura:
    if figura == "Cubo":
        st.pyplot(graficar_cubo(lado))

    elif figura == "Esfera":
        st.pyplot(graficar_esfera(radio))

    elif figura == "Cilindro":
        st.pyplot(graficar_cilindro(radio, altura))

    elif figura == "Piramide":
        st.pyplot(graficar_piramide(l_base, altura))


#Materiales
st.subheader("Material")
tiene_material = st.radio(
    "¿La figura tiene un material asociado?",
    ["No", "Si"],
    horizontal=True
)

material = None
densidad = None

if tiene_material == "Si":
    lista_materiales = list(densidades.keys())
    material = st.selectbox("Elige el material:", lista_materiales)
    densidad = densidades[material]
    st.caption(f"Densidad de {material}: {densidad} kg/m^3")

st.divider()


#calculos y botones

if st.button("Calcular", type="primary"):
    if figura == "Cubo":
        lado_m = convertir_longitud(lado, u_entrada, "m")
        a_m2, v_m3, formulas = calcular_cubo(lado_m)

    elif figura == "Esfera":
        rm = convertir_longitud(radio, u_entrada, "m")
        a_m2, v_m3, formulas = calcular_esfera(rm)

    elif figura == "Cilindro":
        rm = convertir_longitud(radio, u_entrada, "m")
        hm = convertir_longitud(altura, u_entrada, "m")
        a_m2, v_m3, formulas = calcular_cilindro(rm, hm)

    elif figura == "Piramide":
        lbm = convertir_longitud(l_base, u_entrada, "m")
        hm = convertir_longitud(altura, u_entrada, "m")
        am = convertir_longitud(apotema, u_entrada, "m")
        a_m2, v_m3, formulas = calcular_piramide(lbm, hm, am)

    area = convertir_area(a_m2, "m", u_salida)
    vol = convertir_vol(v_m3, "m", u_salida)

    masa = None
    if densidad:
        masa = densidad * v_m3

    #Mostrar resultados 
    st.success(f"Resultados para: {figura}")

    st.markdown(f"**{formulas['area']}**")
    st.metric(f"Area ({u_salida}^2)", f"{area:.4f}")

    st.markdown(f"**{formulas['volumen']}**")
    st.metric(f"Volumen ({u_salida}^3)", f"{vol:.4f}")

    if masa:
        st.markdown("**Masa = Densidad * Volumen**")
        st.metric("Masa (kg)", f"{masa:.4f}")

    #Guardar el resultado en el historial de la sesion
    st.session_state.rslt.append({
        "nombre": figura,
        "area": area,
        "volumen": vol,
        "unidad": u_salida,
        "formulas": formulas,
        "material": material,
        "densidad": densidad,
        "masa": masa
    })

st.divider()




#Historial resultados
st.subheader("Historial de figuras calculadas")
if st.session_state.rslt:
    filas = []
    for idx, r in enumerate(st.session_state.rslt, start=1):
        filas.append({
            "N°": idx,
            "Figura": r["nombre"],
            f"Area ({r['unidad']}²)": round(r["area"], 4),
            f"Volumen ({r['unidad']}³)": round(r["volumen"], 4),
            "Material": r["material"] if r["material"] else "—",
            "Masa (kg)": round(r["masa"], 4) if r["masa"] else "—",
        })

    tabla = pd.DataFrame(filas).set_index("N°")
    st.dataframe(tabla, use_container_width=True)

    st.markdown("#### Detalle de cada figura")

#detalles completos

    for idx, r in enumerate(st.session_state.rslt, start=1):
        with st.container(border=True):
            st.markdown(f"**Figura {idx}: {r['nombre']}**")

            c1, c2 = st.columns(2)
            with c1:
                st.caption(r["formulas"]["area"])
                st.metric(f"Area ({r['unidad']}²)", f"{r['area']:.4f}")
            with c2:
                st.caption(r["formulas"]["volumen"])
                st.metric(f"Volumen ({r['unidad']}³)", f"{r['volumen']:.4f}")

            if r["material"]:
                st.caption(f"Material: {r['material']} · Densidad: {r['densidad']} kg/m³ · Masa = Densidad × Volumen")
                st.metric("Masa (kg)", f"{r['masa']:.4f}")

    col_a, col_b = st.columns(2)

    with col_a:
        reporte = generar_reporte(st.session_state.rslt)
        st.download_button(
            label="Descargar reporte (.txt)",
            data=reporte,
            file_name="resultados.txt",
            mime="text/plain"
        )

    with col_b:
        if st.button("Borrar historial"):
            st.session_state.rslt = []
            st.rerun()

else:
    st.info("Todavia no se ha calculado ninguna figura.")

