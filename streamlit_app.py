import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="SMART MED NURSE", layout="wide")

st.title("🧠 SMART MED NURSE – MVP")

menu = st.sidebar.selectbox(
    "Выберите модуль:",
    ["Чат-консультация", "Документация 003/у",
     "Справочник МЗ РК", "Расчеты и графики", "Напоминания"]
)

if menu == "Чат-консультация":
    st.header("Чат поддержки медсестры")
    user_input = st.text_area("Введите клиническую ситуацию")

    if st.button("Получить алгоритм"):
        st.success("Алгоритм активирован")
        st.write("• Измерить АД, ЧСС, сатурацию")
        st.write("• Проверить красные флаги")
        st.write("• При необходимости направить к врачу")
        st.write("• Заполнить форму 003/у")

elif menu == "Документация 003/у":
    st.header("Форма 003/у")

    name = st.text_input("ФИО пациента")
    age = st.number_input("Возраст", min_value=0)
    complaints = st.text_area("Жалобы")

    if st.button("Сформировать запись"):
        st.subheader("Сформированная запись")
        st.write(f"Пациент: {name}")
        st.write(f"Возраст: {age}")
        st.write(f"Жалобы: {complaints}")
        st.write("Объективно: состояние стабильное.")
        st.write("Рекомендации: симптоматическая терапия.")

elif menu == "Справочник МЗ РК":
    st.header("Нормативная база")

    query = st.text_input("Введите запрос")

    if st.button("Найти информацию"):
        st.info("Ключевые пункты:")
        st.write("• Контроль температуры")
        st.write("• Мониторинг сатурации")
        st.write("• Критерии госпитализации")

elif menu == "Расчеты и графики":
    st.header("Расчеты")

    weight = st.number_input("Вес (кг)")
    height = st.number_input("Рост (см)")

    if st.button("Рассчитать ИМТ"):
        if height > 0:
            bmi = weight / ((height/100)**2)
            st.success(f"ИМТ: {round(bmi,2)}")

    st.subheader("График температуры")
    temps = st.text_input("Введите значения через запятую")

    if st.button("Построить график"):
        try:
            temp_list = [float(x) for x in temps.split(",")]
            fig, ax = plt.subplots()
            ax.plot(temp_list)
            ax.set_xlabel("Дни")
            ax.set_ylabel("Температура")
            st.pyplot(fig)
        except:
            st.error("Ошибка ввода")

elif menu == "Напоминания":
    st.header("План задач")

    task = st.text_input("Введите задачу")
    date = st.date_input("Дата")

    if st.button("Добавить задачу"):
        st.success(f"Задача '{task}' назначена на {date}")
