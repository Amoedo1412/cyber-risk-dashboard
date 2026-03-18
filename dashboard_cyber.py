import streamlit as st
import pandas as pd
import psycopg2
import matplotlib.pyplot as plt

# Configuração da Página
st.set_page_config(page_title="SIEM Risk Dashboard", layout="wide")
st.title("🛡️ Painel de Gestão de Risco de Cibersegurança")

# Função para ligar à BD
def get_data():
    conn = psycopg2.connect(
        host="localhost", database="postgres", 
        user="postgres", password="R4f4eL_2oo5:Pr0ject"
    )
    query = """
        SELECT a.nome, i.tipo_ataque, a.custo_paragem_hora 
        FROM incidentes i 
        JOIN ativos a ON i.ativo_id = a.id
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df

try:
    data = get_data()

    # Métrica de Resumo
    total_risco = data['custo_paragem_hora'].sum() * 2
    st.metric(label="💰 Risco Financeiro Total Acumulado", value=f"{total_risco} €")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Ataques por Ativo")
        st.bar_chart(data['nome'].value_counts())

    with col2:
        st.subheader("Distribuição de Tipos de Ataque")
        fig, ax = plt.subplots()
        data['tipo_ataque'].value_counts().plot.pie(autopct='%1.1f%%', ax=ax)
        st.pyplot(fig)

    st.subheader("Dados Brutos dos Incidentes")
    st.write(data)

except Exception as e:
    st.error(f"Erro ao carregar dashboard: {e}")