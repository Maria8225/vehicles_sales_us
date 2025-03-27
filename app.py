import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


#Lee el archivo csv        
car_data = pd.read_csv('vehicles_us.csv')

#Encabezado de la aplicación
st.header("Exploración de ventas de autos en Estados Unidos")

#Botón para construir un histograma
hist_button = st.button('Construir histograma')
        
if hist_button:
    st.write('Creación de un histograma de días en publicación en venta')
            
    # crear un histograma
    fig = px.histogram(car_data,
                   x="days_listed",
                   title="Días en publicación de los vehículos",
                   labels={"days_listed":"Días en publicación"},
                   color="condition",
                   nbins=50)
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

#Botón para crear un gráfico de dispersión
disp_button = st.button('Construir gráfico de dispersión')

if disp_button:
    st.write('Creación de gráfico de dispersión precio vs millas recorridas')

    # Crear un gráfico de dispersión
    fig2 = px.scatter(car_data,
                    x="odometer",  
                    y="price",  
                    title="Precio vs Millas recorridas",
                    labels={"odometer": "Millas recorridas (M)", "price": "Precio (USD)"},
                    color="type",) 

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig2, use_container_width=True)

#Botón para mostrar información básica de vehículos en venta
disp_button = st.button('Construir tabla con datos exploratorios de los vehículos')

if disp_button:
    st.write('Creación de tabla con información general de los vehículos en venta')

    # Crear tabla con información básica
    fig3 = go.Figure(data=[go.Table(header=dict(values=["type","condition","transmission","odometer","price"],
                fill_color='paleturquoise',
                align='left'),
                cells=dict(values=[car_data.type, car_data.condition, car_data.transmission, car_data.odometer, car_data.price],
                fill_color='lavender',
                align='left'))
                ])

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig3, use_container_width=True)
