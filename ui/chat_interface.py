import streamlit as st
import requests

def title():
    st.set_page_config(page_title="ChatRAD", page_icon="🤖")
    st.markdown(
        "<h1 style='text-align: center'>Chat<span style='color:blue;'>RAD</span>: Assistente de Análise de Radiografias Torácicas 🩻</h1>", 
        unsafe_allow_html=True
    )

# Armazenar o histórico de mensagens
def store_message(type_user, prompt, buttons=None):
    if "exists_button" not in st.session_state:
        st.session_state["exists_button"] = False
    new_msg = {"sender": type_user, "message": prompt}
    if "msg" in st.session_state:
        msg = st.session_state["msg"]
        #se houver botoes, cria nova chave e valor para o botao
        if buttons:
            st.session_state["exists_button"] = True
            new_msg["buttons"] = buttons
        else:
            st.session_state["exists_button"] = False
    else:
        msg = []
        st.session_state["msg"] = msg

    msg.append(new_msg)
    return msg

# Cria os balões de texto do chat
def create_ballon(type_user, image, message):
    with st.chat_message(type_user, avatar=image):
        st.write(message)

def get_rasa_responses(prompt):
    # Definição do endereço do RASA
    rasa_url = "http://localhost:5005/webhooks/rest/webhook"
    payload = {"sender": "user_1", "message": prompt}

    try:
        #tenta enviar o payload para o rasa por JSON e ja transforma em uma lista python
        response = requests.post(rasa_url, json=payload)
        return response.json()
    except:
        return [{"text": "Erro: O servidor Rasa está offline. 🔴"}]

def get_service_entity():
    url = "http://localhost:5005/conversations/user_1/tracker"
    try:
        response = requests.get(url)
        data = response.json()
        
        entities = data.get("latest_message", {}).get("entities", [])
        
        if entities:
            # Retorna o valor (ex: 'laudo') para bater com seu IF
            return entities[0].get("value")
            
        return None
    except Exception as e:
        print(f"Erro ao acessar Tracker: {e}")
        return None

def main():
    title()
    if "msg" not in st.session_state:
        st.session_state["msg"] = []
    msg = st.session_state["msg"]

    for i, m in enumerate(msg):
        # mensagem do usuário na tela
        if m["sender"] == "user":
            create_ballon(m["sender"], "https://cdn-icons-png.flaticon.com/512/9439/9439123.png", m["message"])
        # mensagem do assistente na tela
        else:
            create_ballon(m["sender"], "https://cdn-icons-png.flaticon.com/512/10817/10817299.png", m["message"])
            if "buttons" in m:
                for btn in m["buttons"]:
                    if st.button(btn["title"], width="stretch", key=f"{btn['payload']}_{i}"):
                        store_message("user", btn["title"])
                        response = get_rasa_responses(btn["payload"])
                        for r in response:
                            store_message("assistant", r.get("text", ""), r.get("buttons"))
                        st.rerun()
                entity_image = ["laudo", "patologico", "similar"]
                entity = get_service_entity()
                if entity in entity_image:
                    uploaded_files = st.file_uploader("Agora envie os exames aqui para prosseguir o atendimento: ", accept_multiple_files=True, type=["jpg", "png"], key=f"upload_{i}")
                    if uploaded_files:
                        st.success("imagem(ns) carregada(s) com sucesso!")
                        #baixar modulos aqui

    prompt = st.chat_input("Como o ChatRAD pode ajudar hoje?")
    # se alguma mensagem foi enviada:
    if prompt:
            # recebe a ultima mensagem adcionada no histórico de mensagens
            msg = store_message("user", prompt)

            #msg de resposta,
            response = get_rasa_responses(prompt)
            for r in response:
                store_message("assistant", r.get("text", ""), r.get("buttons"))
            st.rerun()
if __name__ == "__main__":
    main()
    


    


