import streamlit as st
import streamlit.components.v1 as components

# Lê o conteúdo do arquivo HTML
with open("desafio.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Exibe o HTML dentro do Streamlit
components.html(html_content, height=800, scrolling=True)
