import streamlit as st
import psycopg2
import funcoes as f

estilo_css = """
<style>
    /* Mudando a cor de fundo do app */
    .stApp {
        background-color: #f0f2f6;
    }
    
    /* Customizando um botão específico */
    div.stButton > button:first-child {
        background-color: #ff4b4b;
        color: white;
        border-radius: 5px;
        border: none;
    }
</style>
"""

def get_id(e_mail, senha, c):
    cursor = c.cursor()
    consulta = "SELECT ID FROM USUARIO WHERE E_MAIL = %s AND SENHA = %s"
    cursor.execute(consulta, (e_mail, senha))
    resultado = cursor.fetchone()
    cursor.close()
    if resultado:
        return resultado[0]
    return None

def interface(c):
    with st.container(border=True):
        st.write("Login de Usuário")
        
        # Início do formulário
        with st.form(key="form_login"):
            email = st.text_input("E-mail: ")
            senha = st.text_input("Senha: ", type="password")
            
            # Botão obrigatório para submeter o formulário
            submit = st.form_submit_button("Login")
            
            if submit:
                if not email or not senha:
                    st.warning("Tente novamente! Algum dado não foi escrito.")
                else:
                    id_encontrado = get_id(email, senha, c)
                    if id_encontrado:
                        st.session_state.usuario_id = id_encontrado
                        st.switch_page("pages/chat_interface.py")
                        st.stop()
                    else:
                        st.error("Esse login não é válido!")
        
        if st.button("Não tem conta ainda?"):
            st.switch_page("cadastro.py")
            st.stop()
def main():
    c = f.conexao()
    interface(c)

if __name__ == "__main__":
    main()