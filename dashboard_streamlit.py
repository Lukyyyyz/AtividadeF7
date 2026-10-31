import os
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configuração da página
st.set_page_config(
    page_title="Dashboard - Atividade 06",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilo personalizado para os gráficos
sns.set_theme(style="whitegrid")

# ---------------------------------------------------------
# SIDEBAR - Informações do Aluno
# ---------------------------------------------------------
with st.sidebar:
    st.header("👤 Informações do Aluno")
    st.markdown("---")
    
    # Preencha com os seus dados pessoais
    nome = st.text_input("Nome do Aluno", value="Seu Nome Aqui")
    chamada = st.text_input("Número da Chamada", value="00")
    turma = st.text_input("Turma", value="Turma X")
    
    st.markdown("---")
    st.markdown("**Atividade 06** - Visualização de Dados")
    st.info("💡 A barra lateral pode ser recolhida utilizando a seta no topo superior esquerdo.")

# ---------------------------------------------------------
# TÍTULO PRINCIPAL
# ---------------------------------------------------------
st.title("📊 Dashboard de Análise de Dados - Atividade 06")
st.write("Visualização consolidada dos gráficos produzidos durante a atividade prática.")
st.markdown("---")

# ---------------------------------------------------------
# CARREGAMENTO DOS DADOS (CSV)
# ---------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DADOS_DIR = os.path.join(BASE_DIR, "dados")

def ler_csv_seguro(nome_arquivo, col_padrao=None):
    caminho = os.path.join(DADOS_DIR, nome_arquivo)
    if os.path.exists(caminho):
        return pd.read_csv(caminho)
    else:
        # Gerador fallback para simular caso o arquivo de dados não esteja no diretório correto
        np.random.seed(42)
        if nome_arquivo == "dados_barras.csv":
            return pd.DataFrame({"Categoria": ["A", "B", "C", "D"], "Valores": [25, 40, 15, 30]})
        elif nome_arquivo == "dados_pizza.csv":
            return pd.DataFrame({"Categoria": ["Item A", "Item B", "Item C"], "Quantidade": [45, 35, 20]})
        elif nome_arquivo == "dados_linhas.csv":
            return pd.DataFrame({"EixoX": [1, 2, 3, 4, 5], "Valores": [10, 20, 15, 25, 30]})
        elif nome_arquivo in ["dados_distribuicao.csv", "dados_frequencia.csv"]:
            return pd.DataFrame({"Valores": np.random.normal(50, 10, 200)})
        elif nome_arquivo == "dados_boxplot.csv":
            return pd.DataFrame({"Grupo": ["G1"]*50 + ["G2"]*50, "Valores": np.random.randn(100)})
        elif nome_arquivo in ["dados_dispersao.csv", "dados_regressao.csv"]:
            x = np.linspace(0, 10, 50)
            return pd.DataFrame({"X": x, "Y": x * 2 + np.random.normal(0, 2, 50)})
        elif nome_arquivo == "dados_heatmap.csv":
            return pd.DataFrame(np.random.rand(5, 5), columns=["A", "B", "C", "D", "E"])
        return pd.DataFrame()

# Carregando dataframes
df_barras = ler_csv_seguro("dados_barras.csv")
df_pizza = ler_csv_seguro("dados_pizza.csv")
df_linhas = ler_csv_seguro("dados_linhas.csv")
df_distribuicao = ler_csv_seguro("dados_distribuicao.csv")
df_frequencia = ler_csv_seguro("dados_frequencia.csv")
df_boxplot = ler_csv_seguro("dados_boxplot.csv")
df_dispersao = ler_csv_seguro("dados_dispersao.csv")
df_regressao = ler_csv_seguro("dados_regressao.csv")
df_heatmap = ler_csv_seguro("dados_heatmap.csv")

# ---------------------------------------------------------
# LINHA 1 DE GRÁFICOS (1 a 3)
# ---------------------------------------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("1. Gráfico de Barras")
    fig, ax = plt.subplots(figsize=(5, 4))
    cols = df_barras.columns
    sns.barplot(data=df_barras, x=cols[0], y=cols[1], ax=ax, palette="Blues_d")
    ax.set_title("Comparação por Categoria")
    st.pyplot(fig)
    st.markdown("""
    **Análise:** 
    O gráfico de barras possibilita comparar os totais entre categorias discretas. 
    Permite identificar visualmente quais grupos se destacam com os maiores ou menores valores.
    """)

with col2:
    st.subheader("2. Gráfico de Pizza")
    fig, ax = plt.subplots(figsize=(5, 4))
    cols = df_pizza.columns
    ax.pie(df_pizza[cols[1]], labels=df_pizza[cols[0]], autopct='%1.1f%%', colors=sns.color_palette("pastel"))
    ax.set_title("Distribuição Proporcional")
    st.pyplot(fig)
    st.markdown("""
    **Análise:** 
    O gráfico de pizza destaca a proporção individual em relação ao todo (100%), facilitando 
    a identificação do peso percentual de cada categoria no universo analisado.
    """)

with col3:
    st.subheader("3. Gráfico de Linhas")
    fig, ax = plt.subplots(figsize=(5, 4))
    cols = df_linhas.columns
    sns.lineplot(data=df_linhas, x=cols[0], y=cols[1], marker="o", ax=ax, color="darkgreen")
    ax.set_title("Evolução Temporal / Tendência")
    st.pyplot(fig)
    st.markdown("""
    **Análise:** 
    O gráfico de linhas evidencia a variação dos dados ao longo de uma sequência continua. 
    Ideal para mapear tendências de alta, queda ou estabilidade nos valores.
    """)

st.markdown("---")

# ---------------------------------------------------------
# LINHA 2 DE GRÁFICOS (4 a 6)
# ---------------------------------------------------------
col4, col5, col6 = st.columns(3)

with col4:
    st.subheader("4. Gráfico de Distribuição")
    fig, ax = plt.subplots(figsize=(5, 4))
    cols = df_distribuicao.columns
    sns.histplot(df_distribuicao[cols[0]], kde=True, ax=ax, color="teal")
    ax.set_title("Densidade e Distribuição")
    st.pyplot(fig)
    st.markdown("""
    **Análise:** 
    Exibe a forma como os dados contínuos estão distribuídos, permitindo analisar a assimetria 
    e a probabilidade das observações em torno da média.
    """)

with col5:
    st.subheader("5. Histograma de Frequência")
    fig, ax = plt.subplots(figsize=(5, 4))
    cols = df_frequencia.columns
    ax.hist(df_frequencia[cols[0]], bins=8, color="coral", edgecolor="black")
    ax.set_title("Contagem por Intervalo")
    ax.set_ylabel("Frequência Absoluta")
    st.pyplot(fig)
    st.markdown("""
    **Análise:** 
    Agrupa dados numéricos em faixas de valores (*bins*), demonstrando onde está concentrado 
    o maior volume de ocorrências do dataset.
    """)

with col6:
    st.subheader("6. Gráfico Boxplot")
    fig, ax = plt.subplots(figsize=(5, 4))
    cols = df_boxplot.columns
    if len(cols) > 1:
        sns.boxplot(data=df_boxplot, x=cols[0], y=cols[1], ax=ax, palette="Set2")
    else:
        sns.boxplot(data=df_boxplot, y=cols[0], ax=ax, color="plum")
    ax.set_title("Dispersão e Outliers")
    st.pyplot(fig)
    st.markdown("""
    **Análise:** 
    Apresenta a síntese dos cinco números (mínimo, $Q_1$, mediana, $Q_3$, máximo). 
    É fundamental para avaliar a variabilidade e identificar a presença de *outliers*.
    """)

st.markdown("---")

# ---------------------------------------------------------
# LINHA 3 DE GRÁFICOS (7 a 9)
# ---------------------------------------------------------
col7, col8, col9 = st.columns(3)

with col7:
    st.subheader("7. Gráfico de Dispersão")
    fig, ax = plt.subplots(figsize=(5, 4))
    cols = df_dispersao.columns
    sns.scatterplot(data=df_dispersao, x=cols[0], y=cols[1], ax=ax, color="indigo")
    ax.set_title("Relação entre Duas Variáveis")
    st.pyplot(fig)
    st.markdown("""
    **Análise:** 
    Exibe a relação individual entre dois atributos numéricos, sendo útil para diagnosticar 
    se existe algum padrão de agrupamento ou correlação aparente.
    """)

with col8:
    st.subheader("8. Gráfico de Regressão")
    fig, ax = plt.subplots(figsize=(5, 4))
    cols = df_regressao.columns
    sns.regplot(data=df_regressao, x=cols[0], y=cols[1], ax=ax, color="darkred")
    ax.set_title("Linha de Ajuste / Tendência Linear")
    st.pyplot(fig)
    st.markdown("""
    **Análise:** 
    Modela o relacionamento linear entre as variáveis $X$ e $Y$. A inclinação da reta indica o sentido 
    e a força da relação estimada.
    """)

with col9:
    st.subheader("9. Mapa de Calor (Heatmap)")
    fig, ax = plt.subplots(figsize=(5, 4))
    sns.heatmap(df_heatmap.corr() if not df_heatmap.empty else df_heatmap, annot=True, cmap="coolwarm", ax=ax, fmt=".2f")
    ax.set_title("Matriz de Correlação")
    st.pyplot(fig)
    st.markdown("""
    **Análise:** 
    Representa os valores da matriz por meio de tonalidades de cores, permitindo identificar 
    rapidamente associações fortes (positivas ou negativas) entre múltiplos atributos.
    """)