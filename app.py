import pandas as pd
import plotly.express as px
import streamlit as st
st.header('Analisis Rapido de Vehiculos')
car_data = pd.read_csv('vehicles_us.csv')
st.dataframe(car_data)
hist_button = st.button(
    'Construir histograma de Distribución de Transmisiones')
if hist_button:
    st.subheader('Distribución de Transmisiones')
    fig = px.histogram(car_data, x="transmission")  # crear un histograma
    # actualizar título del gráfico
    fig.update_layout(title_text='Distribución de Transmisiones')
    # actualizar título del eje x
    fig.update_xaxes(title_text='Tipo de Transmisión')
    # actualizar título del eje y
    fig.update_yaxes(title_text='Frecuencia de venta')
    # actualizar trazas del gráfico
    fig.update_traces(marker=dict(line=dict(width=1, color='black')))
    fig.update_yaxes(type='log')  # actualizar eje y a escala logarítmica

    st.plotly_chart(fig)

hist_button2 = st.button('Construir histograma de Distribución del tipo de combustible'
                         )
if hist_button2:
    st.subheader('Distribución del tipo de combustible')
    fig = px.histogram(car_data, x="fuel")  # crear un histograma
    # actualizar título del gráfico
    fig.update_layout(title_text='Distribución del tipo de combustible')
    # actualizar título del eje x
    fig.update_xaxes(title_text='Tipo de Combustible')
    # actualizar título del eje y
    fig.update_yaxes(title_text='Frecuencia de venta')
    # actualizar trazas del gráfico
    fig.update_traces(marker=dict(line=dict(width=1, color='black')))
    fig.update_yaxes(type='log')  # actualizar eje y a escala logarítmica

    st.plotly_chart(fig)

hist_button3 = st.button(
    'Consrtuir Grafico de Dispercion de Kilometros y Precio')
if hist_button3:
    st.subheader('Relación entre Kilómetros y Precio')
    fig = px.scatter(car_data, x="odometer", y="price", labels={
                     "odometer": "Kilómetros", "price": "Precio"})  # crear un gráfico de dispersión
    # actualizar título del gráfico
    fig.update_layout(title_text='Relación entre Kilómetros y Precio')
    fig.update_xaxes(title_text='Kilómetros')  # actualizar título del eje x
    fig.update_yaxes(title_text='Precio')  # actualizar título del eje y

    st.plotly_chart(fig)  # mostrar gráfico de dispersión en Streamlit

hist_button4 = st.button(
    'Construir Grafico de comparacion de Tipo de propulsion')
if hist_button4:
    st.subheader('Comparación de Tipo de Propulsión')
    car_count_df = car_data.groupby(
        ['model', 'fuel']).size().reset_index(name='count')
    # ordenar por la cantidad de autos vendidos
    car_count_df = car_count_df.sort_values(by='count')
    fig = px.bar(
        car_count_df,
        x='model',
        y='count',
        color='fuel',
        title=('Cantidad de Autos vendidos por Modelo y tipo de Combustible.')
    )  # crear gráfico de barras
    fig.update_layout(
        xaxis_title='Modelo',
        yaxis_title='Cantidad de Autos Vendidos',
        annotations=[
            dict(
                x=0.5,
                y=-2.4,
                xanchor='center',
                xref='paper',
                yref='paper',
                text='Se recomienda usar solo una categoría de combustible a la vez para poder ver con mayor detalle los más vendidos por tipo de propulsión.',
                showarrow=False,
                font=dict(size=12)
            )
        ]
    )  # agregar pie de gráfico
    # actualizar trazas del gráfico
    fig.update_traces(marker=dict(line=dict(width=1, color='black')))
    fig.update_xaxes(tickangle=90)  # rotar etiquetas del eje x
    # agrupar barras por tipo de combustible
    fig.update_layout(barmode='group')
    st.plotly_chart(fig)  # mostrar gráfico en Streamlit
