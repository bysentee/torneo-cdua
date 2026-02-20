import streamlit as st
import os

# Asegúrate de que este archivo y el archivo HTML (index.html) están en la misma carpeta.
# Python solo lee y envía el HTML al navegador. La lógica del sistema suizo y la rúbrica se ejecutan en el navegador del usuario.

def main():
    try:
        # Leer el archivo HTML (el código de la Versión 12)
        with open("index.html", "r", encoding="utf-8") as f:
            html_content = f.read()
        
        # Mostrar el HTML en la página
        st.markdown(html_content, unsafe_allow_html=True)
        
    except FileNotFoundError:
        st.error("❌ No se encuentra 'index.html'. Asegúrate de que el archivo HTML (el código largo que te di antes) está en la misma carpeta que este archivo Python.")

if __name__ == "__main__":
    main()
