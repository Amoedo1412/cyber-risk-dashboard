import streamlit as st
import pandas as pd
import psycopg2

st.set_page_config(page_title="SIEM Cyber", layout="wide")
st.title("🛡️ Dashboard de Cibersegurança")

# CONFIGURAÇÃO DE LIGAÇÃO
DB_CONFIG = {
    "host": "127.0.0.1",
    "port": "5432",
    "database": "postgres",
    "user": "postgres",
    "password": "R4f4eL_2oo5_Pr0ject"
}

def carregar_dados():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        query = "SELECT a.nome, i.tipo_ataque, a.custo_paragem_hora FROM incidentes i JOIN ativos a ON i.ativo_id = a.id"
        df = pd.read_sql(query, conn)
        conn.close()
        
        # FORÇAR NOMES EM MINÚSCULAS PARA EVITAR ERROS
        if not df.empty:
            df.columns = [str(col).lower() for col in df.columns]
            # Debug: Isto vai aparecer no teu CMD (janela preta)
            print("Colunas encontradas:", df.columns.tolist())
        return df
    except Exception as e:
        st.error(f"Erro de Ligação: {e}")
        return pd.DataFrame()

df = carregar_dados()

if not df.empty:
    st.success("✅ Ligado à Base de Dados com Sucesso!")
    
    # 1. Métrica de Impacto (usamos 'custo_paragem_hora' que é o nome real na BD)
    # Se der erro aqui, tenta df.iloc[:, 2].sum()
    try:
        total = df['custo_paragem_hora'].sum()
        st.metric("💰 Impacto Financeiro Total", f"{total} €")
    except:
        st.metric("💰 Impacto Financeiro Total", "Erro no cálculo")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Volume de Ataques por Ativo")
        # Usamos o nome original da coluna na BD: 'nome'
        if 'nome' in df.columns:
            st.bar_chart(df['nome'].value_counts())
        else:
            st.write("Coluna 'nome' não encontrada.")

    with col2:
        st.subheader("Tipos de Ataques Detectados")
        # Usamos o nome original da coluna na BD: 'tipo_ataque'
        if 'tipo_ataque' in df.columns:
            st.bar_chart(df['tipo_ataque'].value_counts())

    st.subheader("Lista Detalhada de Incidentes")
    st.dataframe(df, use_container_width=True)
    
else:
    st.warning("⚠️ Sem dados. Verifica se inseriste os dados no DBeaver.")