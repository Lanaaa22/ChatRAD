import streamlit as st
import requests
import psycopg2
import funcoes as f

def getId(e_mail, senha, c):
    cursor = c.cursor()
    consulta = "SELECT ID FROM USUARIO WHERE E_MAIL = %s AND SENHA = %s"
    cursor.execute(consulta, (e_mail, senha))
    resultado = cursor.fetchone()
    cursor.close()
    if resultado:
        return resultado[0]
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
        
        with st.form(key="form_cadastro"):
            nome = st.text_input("Nome Completo: ")
            profissao = st.text_input("Profissão: ")
            email = st.text_input("E-mail: ")
            senha = st.text_input("Senha: ", type="password")
            
            submit = st.form_submit_button("Cadastrar")
            
            if submit:
                if not email or not senha or not profissao or not nome:
                    st.warning("Tente novamente! algum dado não foi escrito")
                else:
                    id_encontrado = inserirProfissional(c, nome, profissao, email, senha)
                    st.session_state.usuario_id = id_encontrado
                    st.switch_page("pages/chat_interface.py")
                    st.stop()
        
        if st.button("Já tem conta?"):
            st.switch_page("pages/login.py")
            st.stop()

def main():
    c = f.conexao()
    
    interface(c)

if __name__ == "__main__":
    main()