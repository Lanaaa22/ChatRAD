import streamlit as st
import requests
import psycopg2

def getId(e_mail, senha, c):
    cursor = c.cursor()
    consulta = "SELECT ID FROM USUARIO WHERE E_MAIL = %s AND SENHA = %s"
    cursor.execute(consulta, (e_mail, senha))
    resultado = cursor.fetchone()
    cursor.close()
    if resultado:
        return resultado[0]
    return None

def conexao():
    try:
        conexao = psycopg2.connect(database = "defaultdb", host = "pg-20fe24c4-ilaninhaaa22-0019.i.aivencloud.com", user = "avnadmin", password = "AVNS_dUBTFOg8pU7MRHo_ied", port= "21277", sslmode="require")
        return conexao
    except Exception as e:
        print(f"Erro ao conectar {e}")
        return None

def inserirProfissional(c, nome, profissao, e_mail, senha):
    cursor = c.cursor()
    insert = """
        INSERT INTO USUARIO (nome, senha, profissao, e_mail)
        VALUES (%s, %s, %s, %s)
        RETURNING id
    """
    cursor.execute(insert, (nome, senha, profissao, e_mail))
    id = cursor.fetchone()[0]
    c.commit()
    print("Cadastro feito com sucesso")
    cursor.close()
    return id

def interface(c):
    with st.container(border=True):
        st.write("Cadastro de Usuário")
        nome = st.text_input("Nome Completo: ")
        profissao = st.text_input("Profissão: ")
        email = st.text_input("E-mail: ")
        senha = st.text_input("Senha: ", type="password")
        if st.button("Cadastrar"):
            if not email or not senha or not profissao or not nome:
                st.warning("Tente novamente! algum dado não foi escrito")
            else:
                id_encontrado = inserirProfissional(c, nome, profissao, email, senha)
                st.session_state.usuario_id = id_encontrado
                st.switch_page("pages/chat_interface.py")
        if st.button("Já tem conta?"):
            st.switch_page("pages/login.py")

def main():
    c = conexao()
    
    interface(c)

if __name__ == "__main__":
    main()