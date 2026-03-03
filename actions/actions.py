# # This files contains your custom actions which can be used to run
# # custom Python code.
# #
# # See this guide on how to implement these action:
# # https://rasa.com/docs/rasa/custom-actions


# # This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionReceberImagem(Action):
     def name(self) -> Text:
         return "action_receber_imagem"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]: 
        print("Entrando na action")
        metadata = tracker.latest_message.get("metadata", {}) #retornar o ultimo anexo armazenado
        imagem = metadata.get("image") or metadata.get("file") #pega o valor na chave image ou file
        if imagem:
            return [SlotSet("imagem_path", imagem)]
        return[]
     
class ActionCompreedeOpcao(Action):
     def name(self) -> Text:
         return "action_compreende_opcao"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]: 
        print("Entrando na action")
        numero = tracker.get_slot("opcao") #retorna o que está arumazenado no slot
        if numero:
            numero = numero.strip()
        if numero == "1":
            dispatcher.utter_message("Estamos encaminhando para o módulo de Achados patológicos.")
        elif numero == "2":
            dispatcher.utter_message("Estamos encaminhando para o módulo de Relatórios de radiografias")
        elif numero == "3":
            dispatcher.utter_message("Estamos encaminhando para o módulo de Laudos médicos automáticos")
        else:
            dispatcher.utter_message("Nenhum módulo foi identificado. Escolha 1, 2 ou 3")
        return []