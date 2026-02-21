import streamlit as st

def main():
    try:
        # 1. Leer el archivo HTML
        with open("index.html", "r", encoding="utf-8") as f:
            html_content = f.read()
            # 2. Enviar al navegador
            st.markdown(html_content, unsafe_allow_html=True)
    except FileNotFoundError:
        st.error("❌ No se encuentra el archivo 'index.html'.")
