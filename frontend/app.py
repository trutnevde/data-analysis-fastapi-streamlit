import streamlit as st
import pandas as pd
import requests
import plotly.express as px

# URL для API
API_URL = "http://localhost:8000/upload/"

st.title("Анализ данных с использованием FastAPI и Streamlit")

# Загрузка файла
uploaded_file = st.file_uploader("Загрузите CSV файл", type=["csv"])

if uploaded_file is not None:
    # Отправляем файл на API
    files = {"file": uploaded_file}
    response = requests.post(API_URL, files=files)

    if response.status_code == 200:
        data = response.json()
        st.subheader("Статистика данных:")

        # Отображение информации
        st.write(f"Колонки: {data['columns']}")
        st.write(f"Размер данных: {data['shape']}")
        st.write("Описательная статистика:")
        st.dataframe(pd.DataFrame(data["summary"]))

        # График
        column = st.selectbox("Выберите колонку для построения графика", data["columns"])
        if column in data["summary"]:
            fig = px.bar(x=list(data["summary"][column].keys()), y=list(data["summary"][column].values()),
                         labels={"x": "Метрика", "y": "Значение"}, title=f"Статистика для {column}")
            st.plotly_chart(fig)
    else:
        st.error(f"Ошибка: {response.json().get('error', 'Неизвестная ошибка')}")