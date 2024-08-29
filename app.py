import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Lançamentos Contábeis",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="expanded"
)

data = {
    'ContaNivel1': ['Conta A', 'Conta B', 'Conta C', 'Conta A', 'Conta B', 'Conta C', 'Conta A', 'Conta B', 'Conta C', 'Conta A'],
    'ContaNivel2': ['SubContaA', 'SubContaC', 'SubContaB', 'SubContaA', 'SubContaA', 'SubContaB', 'SubContaA', 'SubContaA', 'SubContaA', 'SubContaB'],
    'Histórico': ['agua', 'luz', 'futebol', 'estoque', 'marketing', 'comercial', 'juridico', 'contabilidade', 'performance', 'outras'],
    'Valor': [1000, 2000, 3000, 150, 250, 350, 5000, 700, 10, 665]
}

df = pd.DataFrame(data)

# Função para mostrar dados filtrados
def show_detailed_view(nivel1, nivel2):
    if nivel1 == 'Exibir Tudo':
        filtered_df = df
    else:
        filtered_df = df[df['ContaNivel1'] == nivel1]
        if nivel2 != 'Todos':
            filtered_df = filtered_df[filtered_df['ContaNivel2'] == nivel2]
    st.write(filtered_df)

# Função principal
def main():
    st.title("Navegação de Contas Contábeis")

    # Seleção de contas de nível 1
    nivel1_accounts = ['Exibir Tudo'] + df['ContaNivel1'].unique().tolist()
    selected_nivel1 = st.sidebar.selectbox("Escolha uma Conta de Nível 1", nivel1_accounts)

    # Atualizar opções de contas de nível 2 com base na seleção de nível 1
    if selected_nivel1 != 'Exibir Tudo':
        nivel2_accounts = ['Todos'] + df[df['ContaNivel1'] == selected_nivel1]['ContaNivel2'].unique().tolist()
        selected_nivel2 = st.sidebar.selectbox("Escolha uma Conta de Nível 2", nivel2_accounts)
    else:
        selected_nivel2 = 'Todos'

    # Mostrar dados filtrados
    show_detailed_view(selected_nivel1, selected_nivel2)

if __name__ == "__main__":
    main()


# numpy
# plotly
# altair
# matplotlib
# mysql-connector-python
# sqlalchemy
# alembic