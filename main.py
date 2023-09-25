from regex import regular_expressions

class JuegoHistoriaInteractiva:
    def __init__(self):
        self.nombre_usuario = None

    def welcome(self):
        print("¡Bienvenido a la Historia Interactiva!")
        self.nombre_usuario = input("Por favor, ingresa tu nombre: ")

    def startGame(self):
        self.welcome()
        print(f"Comencemos, {self.nombre_usuario}.\n")


    def playAgain(self):
        respuesta = input("¿Deseas jugar nuevamente? (Sí/No): ")
        return respuesta.lower() == 'si'


#game = JuegoHistoriaInteractiva()
#game.startGame()

#while game.playAgain():
 #   game.startGame()

#print("Gracias por jugar. ¡Hasta luego!")

print(regular_expressions.validateUsername("Juan"))