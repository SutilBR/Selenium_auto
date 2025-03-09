import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

class Cadastro_notas:
    def __init__(self, banco_nome):
        self.BANCO_DADOS = banco_nome
        with sqlite3.connect(self.BANCO_DADOS) as conn:
            cursor = conn.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS cadastro (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                contrato TEXT,
                nota INTEGER,
                quantidade INTEGER,
                valor INTEGER
            )
            """)
            conn.commit()

        if "contrato" not in st.session_state:
            st.session_state["contrato"] = ""
        if "nota" not in st.session_state:
            st.session_state["nota"] = ""
        if "quantidade" not in st.session_state:
            st.session_state["quantidade"] = 0
        if "valor" not in st.session_state:
            st.session_state["valor"] = 0

        st.title("Cadastro de Notas")

        self.contrato = st.text_input("Contrato")
        self.nota = st.text_input("Preencha o Número da Nota")
        self.quantidade = st.number_input("Preencha a Quantidade da Nota", min_value=0)
        self.valor = st.number_input("Preencha o Valor Total da Nota", min_value=0)

    def cadastrar_nota(self):
        try:
            with sqlite3.connect(self.BANCO_DADOS) as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO cadastro (contrato, nota, quantidade, valor) VALUES (?, ?, ?, ?)", 
                            (self.contrato, self.nota, self.quantidade, self.valor))
                conn.commit()
            st.success("Nota cadastrada")
        except Exception as e:
            st.error(f"Ocorreu um erro, por favor, tente novamente. {e}")

    
    def obter_dados(self):
        conn = sqlite3.connect(self.BANCO_DADOS)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT contrato, COUNT(nota) AS quantidade_notas
            FROM cadastro
            GROUP BY contrato
        """)
        self.dados = cursor.fetchall()
        self.df = pd.DataFrame(self.dados, columns=["Contrato", "Quantidade de Notas"])
        conn.close()
        return self.df

    def exibir_grafico(self):
        self.df = self.obter_dados()
        st.write("Quantidade de Notas por Contrato", self.df)
        fig, ax = plt.subplots()
        ax.bar(self.df["Contrato"], self.df["Quantidade de Notas"], color='blue')
        ax.set_xlabel("Contrato")
        ax.set_ylabel("Quantidade de Notas")
        ax.set_title("Gráfico de Quantidade de Notas por Contrato")
        st.pyplot(fig)

    def buttons_exec(self):
        cadastrar = st.button("Cadastrar")
        if cadastrar:
            self.cadastrar_nota()

BANCO_DADOS = "cadastro.db"
cadastro = Cadastro_notas(BANCO_DADOS)
cadastro.buttons_exec()
cadastro.exibir_grafico()

