import streamlit as st, os, pandas as pd, oracledb, matplotlib.pyplot as plt

conn = oracledb.connect(user='rm562274', password='090402', dsn='oracle.fiap.com.br:1521/ORCL')
cursor = conn.cursor()

# Consulta dados
mes = input('Digite o mês que deseja vizualizar no dashboard')
df = pd.read_sql_query(f"SELECT * FROM sensores where TIME like '%{mes}%' ORDER BY time DESC", conn)

# Título
st.title("Dashboard - Sistema de Irrigação Inteligente")

# Exibe a tabela
st.subheader("Leituras dos Sensores")
st.dataframe(df)

# Gráfico de Umidade
st.subheader("Umidade ao longo do tempo")
st.line_chart(df[['UMIDADE']])

# Gráfico de pH
st.subheader("pH ao longo do tempo")
st.line_chart(df[['PH']])
