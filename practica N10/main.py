import streamlit as st
from figuras import *
from visualizador import Visualizador3DPlotly, cargar_datos, guardar_datos

def main():
    st.title("Visualizador de Superficies 3D")

    tipos = ["Plano", "Paraboloide", "Sinusoide", "Hiperboloide", "Conica", "Toroide", "Cubo", "Piramide", "Cilindro"]
    tipo = st.selectbox("Seleccione el tipo de superficie:", tipos)

    if tipo == "Plano":
        parametro_label = "Pendiente"
        parametro = st.number_input(parametro_label, value=1.0)
        superficie = Plano((-5, 5), (-5, 5), parametro)
    elif tipo == "Paraboloide":
        parametro_label = "Coeficiente"
        parametro = st.number_input(parametro_label, value=1.0)
        superficie = Paraboloide((-5, 5), (-5, 5), parametro)
    elif tipo == "Sinusoide":
        parametro_label = "Frecuencia"
        parametro = st.number_input(parametro_label, value=1.0)
        superficie = Sinusoide((-5, 5), (-5, 5), parametro)
    elif tipo == "Hiperboloide":
        a = st.number_input("a", value=1.0)
        b = st.number_input("b", value=1.0)
        c = st.number_input("c", value=1.0)
        superficie = Hiperboloide((-5, 5), (-5, 5), a, b, c)
    elif tipo == "Conica":
        a = st.number_input("a", value=1.0)
        b = st.number_input("b", value=1.0)
        superficie = Conica((-5, 5), (-5, 5), a, b)
    elif tipo == "Toroide":
        R = st.number_input("R", value=1.0)
        r = st.number_input("r", value=0.5)
        superficie = Toroide((-5, 5), (-5, 5), R, r)
    elif tipo == "Cubo":
        lado = st.number_input("Lado", value=1.0)
        superficie = Cubo(lado)
    elif tipo == "Piramide":
        base = st.number_input("Base", value=1.0)
        altura = st.number_input("Altura", value=1.0)
        superficie = Piramide(base, altura)
    elif tipo == "Cilindro":
        radio = st.number_input("Radio", value=1.0)
        altura = st.number_input("Altura", value=1.0)
        superficie = Cilindro(radio, altura)

    if st.button("Visualizar"):
        visualizador = Visualizador3DPlotly(superficie)
        visualizador.mostrar_con_plotly()
        x, y, z = superficie.generar_datos()
        guardar_datos(x, y, z)

    st.subheader("O cargar datos desde un archivo")
    cargar_datos()

if __name__ == "__main__":
    main()
