import streamlit as st
import requests
import psycopg2
import streamlit

def get_id(e_mail, cursor):
    usuario_no_banco = cursor.execute("SELECT id FROM usuario WHERE e_mail = %s", (e_mail,))
    result = cursor.fetchone()

    if result:
        st.session_state['usuario_id'] = result[0]
    return None



def conexao():
    try:
        conexao = psycopg2.connect(database = "defaultdb", host = "pg-20fe24c4-ilaninhaaa22-0019.i.aivencloud.com", user = "avnadmin", password = "AVNS_dUBTFOg8pU7MRHo_ied", port= "21277", sslmode="require")
        print("Conexão realizada com sucesso")
        return conexao
    except Exception as e:
        print(f"Erro ao conectar {e}")
        return None

def validarProfissional(c, cursor, e_mail, senha):
    cursor.execute("SELECT ID FROM USUARIO WHERE E_MAIL = %s AND SENHA = %s", (e_mail, senha))
    return cursor.fetchone()


def interface(c, cursor):
    with st.container(border=True):
        st.write("Login de Usuário")
        email = st.text_input("E-mail: ")
        senha = st.text_input("Senha: ", type="password")
        get_id(email, cursor)
        if st.button("Login"):
            if not email or not senha:
                st.write("Tente novamente! algum dado não foi escrito")
            else:
                valido = validarProfissional(c, cursor, email, senha)
                if valido:
                    st.switch_page("pages/chat_interface.py")
                else:
                    st.write("Esse login não é válido!")
        if st.button("Não tem conta ainda?"):
            
            st.switch_page("cadastro.py")
def main():
    c = conexao()
    cursor = c.cursor()
    interface(c, cursor)

if __name__ == "__main__":
    main()