# 🛡️ SIEM Risk Dashboard - Monitorização de Cibersegurança

Este projeto é um protótipo de um sistema **SIEM (Security Information and Event Management)** simplificado, focado na interseção entre **Cibersegurança** e **Informática de Gestão**. O sistema monitoriza incidentes em tempo real e calcula o impacto financeiro baseado na criticidade dos ativos.

## 🚀 Funcionalidades
- **Ingestão de Dados:** Registo de ataques (Brute Force, SQL Injection, DDoS, etc.) numa base de dados relacional.
- **Cálculo de Risco:** Estimativa automática de prejuízo financeiro baseada no `custo_paragem_hora` de cada ativo afetado.
- **Dashboard Interativo:** Visualização de métricas e gráficos de volume de ataques por ativo e por tipo.

## 🛠️ Tecnologias Utilizadas
- **Base de Dados:** PostgreSQL (Gestão de ativos e logs de incidentes).
- **Linguagem:** Python 3.14.
- **Bibliotecas:** - `Streamlit`: Para a interface web.
  - `Pandas`: Para manipulação e análise de dados.
  - `Psycopg2`: Para a ponte de ligação Python-PostgreSQL.

## 📋 Como Correr o Projeto
1. **Configurar a BD:** Executar os scripts SQL fornecidos no DBeaver para criar as tabelas `ativos` e `incidentes`.
2. **Instalar Dependências:**
   ```bash
   pip install streamlit pandas psycopg2