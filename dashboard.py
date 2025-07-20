import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Título e descrição
st.title("Dashboard de Indicadores - Sienge ERP")
st.markdown("""
Este dashboard simula KPIs financeiros e operacionais integrados ao ERP Sienge, com dados de vendas, fluxo de caixa e custos por área.
""")

# Simulação de dados
np.random.seed(42)
meses = pd.date_range(start='2024-01-01', periods=12, freq='M').strftime('%b/%Y')

# Vendas mensais simuladas
vendas = np.random.uniform(100000, 250000, size=12).round(2)
fluxo_caixa = np.random.uniform(80000, 220000, size=12).round(2)
custos_engenharia = np.random.uniform(20000, 60000, size=12).round(2)
custos_marketing = np.random.uniform(10000, 30000, size=12).round(2)
custos_administracao = np.random.uniform(15000, 40000, size=12).round(2)

# DataFrame resumo
df = pd.DataFrame({
    'Mês': meses,
    'Vendas (R$)': vendas,
    'Fluxo de Caixa (R$)': fluxo_caixa,
    'Custos Engenharia (R$)': custos_engenharia,
    'Custos Marketing (R$)': custos_marketing,
    'Custos Administração (R$)': custos_administracao
})

# KPIs principais - mostrar os totais e médias do ano
st.header("Principais KPIs Anuais")
col1, col2, col3 = st.columns(3)

col1.metric("Total Vendas (R$)", f"{vendas.sum():,.2f}", f"{((vendas[-1] - vendas[-2]) / vendas[-2] * 100):.2f}% em relação ao mês anterior")
col2.metric("Fluxo de Caixa Total (R$)", f"{fluxo_caixa.sum():,.2f}", f"{((fluxo_caixa[-1] - fluxo_caixa[-2]) / fluxo_caixa[-2] * 100):.2f}% em relação ao mês anterior")
col3.metric("Custo Total (R$)", f"{(custos_engenharia + custos_marketing + custos_administracao).sum():,.2f}", "")

# Gráfico de vendas e fluxo de caixa
st.header("Vendas e Fluxo de Caixa Mensal")
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(meses, vendas, marker='o', label='Vendas')
ax.plot(meses, fluxo_caixa, marker='o', label='Fluxo de Caixa')
ax.set_ylabel("R$ (milhares)")
ax.set_xticklabels(meses, rotation=45)
ax.grid(True)
ax.legend()
st.pyplot(fig)

# Gráfico de custos por área
st.header("Custos Mensais por Área")
fig2, ax2 = plt.subplots(figsize=(10, 5))
ax2.bar(meses, custos_engenharia, label='Engenharia')
ax2.bar(meses, custos_marketing, bottom=custos_engenharia, label='Marketing')
bottom_stack = custos_engenharia + custos_marketing
ax2.bar(meses, custos_administracao, bottom=bottom_stack, label='Administração')
ax2.set_ylabel("R$ (milhares)")
ax2.set_xticklabels(meses, rotation=45)
ax2.legend()
st.pyplot(fig2)

# Mostrar tabela completa
st.header("Tabela de Dados")
st.dataframe(df.style.format("{:,.2f}"))

# Rodapé
st.markdown("---")
st.markdown("📊 Dashboard criado por Gustavo Farias - Data Analyst")

