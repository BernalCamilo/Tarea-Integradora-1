from regex import regular_expressions
from automata import automata as non_finite_automata
from story_elements.transitions import nfa_transitions as nfa_t
from story_elements import story as stry




class JuegoHistoriaInteractiva:

    

    def start_story(self):
       
        nfa_transitions = nfa_t.transitions     
        history = stry.story
        nfa = non_finite_automata.nfa

        current_position = 0
        ans = ""

        print(history[0])
        while current_position < len(nfa_transitions):
            transitions = nfa_transitions[current_position]
            if not transitions:
                if (nfa.accepts(ans)):
                    print("Felicidades, has sobrevivido")
                else:
                    print("Lo siento, HAZ MUERTO")
                break

            
            for idx, next_state in enumerate(transitions):
                print(f"{idx}: {history[next_state]}")

            user_choice = input("Elija un número para avanzar (o 'q' para salir): ")

            if user_choice == 'q':
                break

            if user_choice.isnumeric():
                choice_idx = int(user_choice)    
                if 0 <= choice_idx < len(transitions):
                    next_state = transitions[choice_idx]
                    current_position = next_state
                    ans = ans + str(choice_idx)
                else:
                    print("Selección inválida. Por favor, elija un número válido de las opciones disponibles.")
            else:
                print("Entrada inválida. Por favor, elija un número válido.")
    
    def __init__(self):
        self.nombre_usuario = None

    def welcome(self):
        print("¡Bienvenido a la Historia Interactiva!")
        self.nombre_usuario = input("Por favor, ingresa tu nombre: ")

    def startGame(self):
        self.welcome()
        print(f"Comencemos, {self.nombre_usuario}.\n")
        self.start_story()
        
    def playAgain(self):
        respuesta = input("¿Deseas jugar nuevamente? (Sí/No): ")
        return respuesta.lower() == 'si'
    
    


game = JuegoHistoriaInteractiva()
game.startGame()



