import streamlit as st
import pandas as pd
from functions import filtro, load_css

st.set_page_config(
    page_title="Lançamentos Contábeis",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_css('style.css')
st.title("Navegação por Centro de Custo")
st.button("Limpar Filtros")


if __name__ == "__main__":
    filtro()


# numpy
# plotly
# altair
# matplotlib
# mysql-connector-python
# sqlalchemy
# alembic