import streamlit as st
import pandas as pd
from database import data
# Função para mostrar dados filtrados
df = pd.DataFrame(pd.read_excel('data.xlsx'))

def show_detailed_view(nivel1, nivel2, search_term):
    if nivel1 == 'Exibir Tudo':
        filtered_df = df
    else:
        filtered_df = df[df['ContaNivel1'] == nivel1]
        if nivel2 != 'Todos':
            filtered_df = filtered_df[filtered_df['ContaNivel2'] == nivel2]

    if search_term:
        filtered_df = filtered_df[filtered_df['Histórico'].str.contains(search_term, case=False, na=False)]

    st.table(filtered_df)

def filtro():
    # Seleção de contas de nível 1
    nivel1_accounts = ['Exibir Tudo'] + df['ContaNivel1'].unique().tolist()
    selected_nivel1 = st.sidebar.selectbox("Escolha uma Conta de Nível 1", nivel1_accounts)

    # Atualizar opções de contas de nível 2 com base na seleção de nível 1
    if selected_nivel1 != 'Exibir Tudo':
        nivel2_accounts = ['Todos'] + df[df['ContaNivel1'] == selected_nivel1]['ContaNivel2'].unique().tolist()
        selected_nivel2 = st.sidebar.selectbox("Escolha uma Conta de Nível 2", nivel2_accounts)
    else:
        selected_nivel2 = 'Todos'

    # Campo de pesquisa por Histórico
    search_term = st.text_input("Pesquisar Histórico")

    # Mostrar dados filtrados   
    show_detailed_view(selected_nivel1, selected_nivel2, search_term)

def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def reset_selectbox():
    st.session_state.selected_nivel1 = 'Exibir Tudo'
    st.session_state.selected_nivel2 = 'Todos'
    st.session_state.search_term = ''