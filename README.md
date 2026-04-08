# ChatRAD 1.0

#### Sistema de conversação para analisar radiografias torácicas desenvolvido com o framework Rasa e uma interface construída no Streamlit

## 🔨 Pré Requisitos

- Instalar o Python (Versão 3.10): https://www.python.org/downloads/

- Instalar o Rasa:
 ```bash
pip install rasa
```

- Instalar o Streamlit:
 ```bash
pip install streamlit
```

- Instalar o ultralytics:
 ```bash
pip install ultralytics
```

## 👾 Compilação e Execução

 ```bash
rasa run --enable-api --cors "*"
```

Em outro terminal:
 ```bash
rasa run actions
```

Em outro terminal:
 ```bash
streamlit run ui/chat_interface.py
```

## Tutorial para o ngrok
https://ngrok.com/docs/getting-started#windows
