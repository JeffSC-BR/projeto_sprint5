import pandas as pd
import streamlit as st
import plotly.express as px

car_data = pd.read_csv('vehicles.csv')
hist_button = st.header('Criar Histograma')

if hist_button:

    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros.')

    fig = px.histogram(car_data, x="odometer")

    st.plotly_chart(fig, use_container_width=True)

build_histogram = st.checkbox('Criar um histograma')

if build_histogram:

    st.write('Criando um histograma para a coluna odometer')

    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

