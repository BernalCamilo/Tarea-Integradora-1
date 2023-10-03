class EventManager:
    def __init__(self):
        self.events = {}

    def add_event(self, event_id, event_data):
        self.events[event_id] = event_data

    def get_event(self, event_id):
        return self.events.get(event_id, None)
    


#Main instance of the EventManager class
events = EventManager()


strange_event = {
    "beginning": {
        "message": "Te encuentras con un forastero misterioso en medio del apocalipsis zombie.",
        "options": [
            {"text": "Saludar al forastero", "next": "saludo_forastero"},
            {"text": "Mantener distancia", "next": "rechazar_forastero"}
        ]
    },
    "saludo_forastero": {
        "message": "Forastero: Soy un sobreviviente.",
        "options": [
            {"text": "Preguntar si es amigo o enemigo", "next": "pregunta_amigo_enemigo"},
            {"text": "Preguntar si necesita ayuda", "next": "pregunta_ayuda"},
        ]
    },
    "pregunta_amigo_enemigo": {
        "message": "Forastero: No soy un zombie.",
        "options": [
            {"text": "No te creo", "next": "rechazo_forastero"},
            {"text": "Continuar la conversación", "next": "continuar_conversacion"},
        ]
    },
    "rechazo_forastero": {
        "message": "Forastero: (Forastero parece ofendido).",
        "options": [
            {"text": "Alejarte", "next": "finalizar"},
        ]
    },
    "pregunta_ayuda": {
        "message": "Forastero: Necesito comida desesperadamente.",
        "options": [
            {"text": "Dar comida", "next": "dar_comida"},
            {"text": "Negarse a ayudar", "next": "negar_ayuda"},
        ]
    },
    "dar_comida": {
        "message": "Forastero: Gracias, eres un buen samaritano.",
        "options": [
            {"text": "Fin", "next": "end"},
        ]
    },
    "negar_ayuda": {
        "message": "Forastero: (Forastero parece decepcionado).",
        "options": [
            {"text": "Alejarte", "next": "finalizar"},
        ]
    },
    "continuar_conversacion": {
        "message": "Forastero: (La conversación continúa).",
        "options": [
            {"text": "Seguir hablando", "next": "continuar_conversacion"},
            {"text": "Alejarte", "next": "end"},
        ]
    },
    "end": {
        "message": "¡Termina el evento especial!"
    }
}


events.add_event(35,strange_event)
