from story_elements.transitions import nfa_transitions as nfa_t
from story_elements import story as stry
from automata import automata as non_finite_automata
from transducers.transducer import Transducer
from regex_expressions import regular_expressions 


class StoryController:
    def __init__(self):
        self.trans = Transducer()
        self.user_name = ""
        self.current_position = 0
        self.nfa_transitions = nfa_t.transitions     
        self.history = stry.story
        self.nfa = non_finite_automata.nfa

    def validate_transitons(self):
        return self.current_position < len(self.nfa_transitions)


    def get_transitions(self):
        return self.nfa_transitions[self.current_position]
    def get_story_state(self,state):
        return self.history[state]
    
    def transduce_text(self,text):
        return self.trans.transductorMethod(self.user_name,text)
    
    def validate_username(self,userName):
        self.user_name = userName
        return regular_expressions.validate_username(userName)