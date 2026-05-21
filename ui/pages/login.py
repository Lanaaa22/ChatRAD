import streamlit as st
import psycopg2

def get_id(e_mail, senha, c):
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
        print("Conexão realizada com sucesso")
        return conexao
    except Exception as e:
        print(f"Erro ao conectar {e}")
        return None

def interface(c):
    with st.container(border=True):
        st.write("Login de Usuário")
        email = st.text_input("E-mail: ")
        senha = st.text_input("Senha: ", type="password")

        if st.button("Login"):
            if not email or not senha:
                st.write("Tente novamente! algum dado não foi escrito")
            else:
                id_encontrado = get_id(email, senha, c)
                if id_encontrado:
                    st.session_state.usuario_id = id_encontrado
                    st.switch_page("pages/chat_interface.py")
                else:
                    st.write("Esse login não é válido!")
        if st.button("Não tem conta ainda?"):
            
            st.switch_page("cadastro.py")
def main():
    c = conexao()
    interface(c)

if __name__ == "__main__":
    main()