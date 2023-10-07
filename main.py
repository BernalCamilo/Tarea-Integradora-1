from regex_expressions import regular_expressions
from automata import automata as non_finite_automata
from story_elements.transitions import nfa_transitions as nfa_t
from story_elements import story as stry
from story_elements import event_manager
from gic import context_free_grammar
from transducers.transducer import Transducer



trans = Transducer()



class Game:
    
    user_name = ""

    def __init__(self):
        self.achievements =[]
        self.events = event_manager.events
    

    def start_story(self):
       
        nfa_transitions = nfa_t.transitions     
        history = stry.story
        nfa = non_finite_automata.nfa

        current_position = 0
        ans = ""

        print(trans.transductorMethod(Game.user_name,history[0]))
        while current_position < len(nfa_transitions):

            
            #Validate special events
            self.validate_events(current_position)

            transitions = nfa_transitions[current_position]
            if not transitions:
                print(ans)
                if (nfa.accepts(ans)):
                    print("Felicidades, has sobrevivido")
                    print("***LOGROS***")
                    for achievement in self.achievements:
                        print(f'Logro: {achievement["achievement"]}\nDescripción: {achievement["description"]}')
                else:
                    print("Lo siento, HAZ MUERTO")
                break

            
            for idx, next_state in enumerate(transitions):
                text = f"{idx}: {history[next_state]}"
                print(trans.transductorMethod(Game.user_name,text))
            print("3: Cambiar nombre de usuario")
            user_choice = input("Elija un número para avanzar (o 'q' para salir): ")

            if user_choice == 'q':
                break
                
            if user_choice.isnumeric():
                choice_idx = int(user_choice) 
                if choice_idx==3:
                    Game.user_name = input("Por favor, ingresa un nuevo nombre: ")
                         
                elif 0 <= choice_idx < len(transitions):
                    next_state = transitions[choice_idx]
                    current_position = next_state
                    ans = ans + str(choice_idx)
                else:
                    print("Selección inválida. Por favor, elija un número válido de las opciones disponibles.")
            else:
                print("Entrada inválida. Por favor, elija un número válido.")
            print("\n")
    

        

    def startGame(self):
        print("¡Bienvenido a la Historia Interactiva!")
        Game.user_name = input("Por favor, ingresa tu nombre: ")
        
        print(f"Comencemos, {Game.user_name}.\n")
        self.start_story()
        
    def playAgain(self):
        respuesta = input("¿Deseas jugar nuevamente? (Sí/No): ")
        return respuesta.lower() == 'si'
    
    def validate_events(self,event_id):
        strange_event = self.events.get_event(event_id)

        consequence = []


        if strange_event is not None:
            print("***EVENTO ESPECIAL***")

            actual_state = "beginning"
            consequence.append("beginning")
            while actual_state != "end":
                interaction = strange_event[actual_state]

                print(interaction["message"])


                for i, option in enumerate(interaction["options"], start=1):
                    print(f"{i}: {option['text']}")
                
                user_choice = input("Elige una opción (ingresa el número correspondiente): ")

                try:
                    user_choice = int(user_choice)
                    if 1 <= user_choice <= len(interaction["options"]):

                        #Add consequence
                        consequence.append(interaction["options"][user_choice-1]["text"].lower().replace(" ", ""))

                        next_interaction = interaction["options"][user_choice - 1]["next"]
                        actual_state = next_interaction
                    else:
                        print("Elección no válida. Por favor, ingresa un número válido.")
                except ValueError:
                    print("Por favor, ingresa un número válido.")
        

        if context_free_grammar.validateachievement(consequence):
            self.achievements.append(self.events.get_achievements(event_id))

    


game = Game()
game.startGame()



