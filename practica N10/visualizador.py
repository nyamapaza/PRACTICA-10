import pandas as pd
import plotly.graph_objects as go
import streamlit as st
from figuras import Cubo, Piramide, Cilindro  # Asegúrate de importar las clases necesarias

class Visualizador3DPlotly:
    def __init__(self, superficie):
        self.superficie = superficie

    def mostrar_con_plotly(self):
        x, y, z = self.superficie.generar_datos()
        if isinstance(self.superficie, (Cubo, Piramide, Cilindro)):
            fig = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z, mode='markers')])
        else:
            fig = go.Figure(data=[go.Surface(z=z, x=x, y=y)])
        fig.update_layout(title='Superficie 3D', autosize=False, width=800, height=800)
        st.plotly_chart(fig)

def cargar_datos():
    archivo_subido = st.file_uploader("Cargar archivo CSV o Excel", type=["csv", "xlsx"])
    if archivo_subido is not None:
        if archivo_subido.name.endswith('.csv'):
            datos = pd.read_csv(archivo_subido)
        else:
            datos = pd.read_excel(archivo_subido)
        
        if {'x', 'y', 'z'}.issubset(datos.columns):
            fig = go.Figure(data=[go.Scatter3d(x=datos['x'], y=datos['y'], z=datos['z'], mode='markers')])
            fig.update_layout(title='Figura 3D desde archivo', autosize=False, width=800, height=800)
            st.plotly_chart(fig)
        else:
            st.error("El archivo debe contener las columnas 'x', 'y' y 'z'.")

def guardar_datos(x, y, z):
    datos = pd.DataFrame({'x': x.flatten(), 'y': y.flatten(), 'z': z.flatten()})
    csv = datos.to_csv(index=False)
    st.download_button(label="Descargar datos como CSV", data=csv, file_name="datos_figura.csv", mime="text/csv")
