import streamlit as st
import pandas as pd
import oracledb
import matplotlib.pyplot as plt

conn = oracledb.connect(user='rm562274', password='090402', dns='oracle.fiap.com.br:1521/ORCL')
df = pd.read_sql_query("SELECT * FROM sensores", conn)

st.title("Dashboard do Sistema de Irrigação")

st.line_chart(df[['umidade']])
st.line_chart(df[['ph']])

st.bar_chart(df['bomba'].value_counts())