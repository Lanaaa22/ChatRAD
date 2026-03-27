# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionCompreendeModulo(Action):
     def name(self) -> Text:
         return "action_compreende_modulo"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]: 
        print("Entrando na action")
        # Identificando o módulo pela entidade "servico"
        modulo = tracker.get_slot("servico")
        if modulo == "patologico":
            dispatcher.utter_message(f"Iniciando o serviço de Identificação de Achados Patológicos")
        elif modulo == "laudo":
            dispatcher.utter_message(f"Iniciando o serviço de Geração de Laudos Automáticos")
        elif modulo == "similar":
            dispatcher.utter_message(f"Iniciando o serviço de Procura de Exames Similares")
        else:
            mensagem_ajuda = (
            "O **ChatRAD** tem como objetivo analisar radiografias torácicas e conta com três funcionalidades principais:\n\n"
            "1. 📝 **Gerar laudo**: Produção de um laudo automático a partir das imagens anexadas.\n"
            "2. 🔍 **Encontrar achados**: Detecção e classificação de achados patológicos.\n"
            "3. 📂 **Exames similares**: Busca exames com padrões parecidos em nosso banco.\n\n"
            "--- \n"
            "Para continuarmos, **selecione um serviço abaixo** e, posteriormente, anexe uma imagem:")

    
            botoes = [
            {"title": "📝 Gerar Laudo", "payload": '/ajuda{"servico": "laudo"}'},
            {"title": "🔍 Encontrar achados patológicos", "payload": '/ajuda{"servico": "patologico"}'},
            {"title": "📂 Encontrar exames similares", "payload": '/ajuda{"servico": "similar"}'}]

            dispatcher.utter_message(text=mensagem_ajuda, buttons=botoes)
        return[]
     
