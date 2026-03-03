import streamlit as st
import requests

if "esperando_imagem" not in st.session_state:
    st.session_state.esperando_imagem = False

st.title("Bem vindo ao ChatRAD!")


RASA_API = "http://localhost:5005/webhooks/rest/webhook"
RASA_PARSE = "http://localhost:5005/model/parse"



if "esperando_imagem" not in st.session_state:
    st.session_state.esperando_imagem = False

if "historicos" not in st.session_state:
    st.session_state.historicos = []

for historico in st.session_state.historicos:
    with st.chat_message(historico["role"]):
        st.markdown(historico["content"])

# ===== ENTRADA =====
if entrada := st.chat_input("Inicialize o diálogo"):

    with st.chat_message("user"):
        st.markdown(entrada)

    st.session_state.historicos.append(
        {"role": "user", "content": entrada}
    )

    # ===== RESPOSTA DO RASA =====
    response = requests.post(
        RASA_API,
        json={"sender": "usuario", "message": entrada}
    )

    data = response.json()
    for r in data:
        bot_msg = r.get("text", "")
        if bot_msg:
            with st.chat_message("assistant"):
                st.markdown(bot_msg)

            st.session_state.historicos.append(
                {"role": "assistant", "content": bot_msg}
            )

    # ===== PARSE (INTENT) =====
    parse = requests.post(
        RASA_PARSE,
        json={"text": entrada}
    ).json()

    if "intent" in parse:
        intent = parse["intent"]["name"]
        print("A intenção usada foi:", intent)
        if intent == "pedirImagem":
            st.session_state.esperando_imagem = True
    else:
        st.error("Intent não encontrada")
        st.write(parse)

if st.session_state.esperando_imagem:
    st.info("Por favor, envie a imagem do seu exame abaixo:") 
    uploaded_files = st.file_uploader("Selecione a imagem", accept_multiple_files=False, type=["jpg", "jpeg", "png"], key="file_uploader")
    if uploaded_files:
        #avisa que a imagem foi recebida ao rasa
        st.session_state.esperando_imagem = False


