import streamlit as st
import requests
import psycopg2

def conexao():
    try:
        conexao = psycopg2.connect(database = "defaultdb", host = "pg-20fe24c4-ilaninhaaa22-0019.i.aivencloud.com", user = "avnadmin", password = "AVNS_dUBTFOg8pU7MRHo_ied", port= "21277", sslmode="require")
        print("Conexão realizada com sucesso")
        return conexao
    except Exception as e:
        print(f"Erro ao conectar {e}")
        return None

def inserirProfissional(c, cursor, nome, profissao, e_mail, senha):
    insert = "INSERT INTO USUARIO (nome, senha, profissao, e_mail) VALUES (%s, %s, %s, %s)"
    values = nome, senha, profissao, e_mail
    cursor.execute(insert, values)
    c.commit()
    print("Cadastro feito com sucesso")

def interface(c, cursor):
    with st.container(border=True):
        st.write("Cadastro de Usuário")
        nome = st.text_input("Nome Completo: ")
        profissao = st.text_input("Profissão: ")
        email = st.text_input("E-mail: ")
        senha = st.text_input("Senha: ", type="password")
        if st.button("Cadastrar"):
            if not email or not senha or not profissao or not nome:
                st.write("Tente novamente! algum dado não foi escrito")
            else:
                inserirProfissional(c, cursor, nome, profissao, email, senha)
                st.switch_page("pages/chat_interface.py")
        if st.button("Já tem conta?"):
            st.switch_page("pages/login.py")

def main():
    c = conexao()
    cursor = c.cursor()
    interface(c, cursor)

if __name__ == "__main__":
    main()