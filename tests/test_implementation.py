from regex_expressions import regular_expressions
from gic import context_free_grammar
from automata import automata as non_deterministic_automata
from transducers.transducer import Transducer
import unittest

class TestRegularExpressions(unittest.TestCase):

    def test_standard_cases(self):
        # Casos estándar
        self.assertTrue(regular_expressions.validate_username("Juan Perez"))
        self.assertTrue(regular_expressions.validate_username("Maria Smith"))
        self.assertTrue(regular_expressions.validate_username("John Doe"))
        self.assertTrue(regular_expressions.validate_username("Juan Duque"))
        self.assertTrue(regular_expressions.validate_username("John"))
        self.assertTrue(regular_expressions.validate_username("Alice Monet"))
        

    def test_limit_cases(self):
        self.assertTrue(regular_expressions.validate_username("J P")) 
        self.assertFalse(regular_expressions.validate_username("user_name 123"))  
        self.assertFalse(regular_expressions.validate_username("Alice123 doe")) 
        self.assertFalse(regular_expressions.validate_username("Alice_Doe"))  
        self.assertFalse(regular_expressions.validate_username("Alice@Doe")) 

    def test_interesting_cases(self):
        self.assertFalse(regular_expressions.validate_username("Alice@Doe"))  
        self.assertTrue(regular_expressions.validate_username("Alice Doe"))  
        self.assertFalse(regular_expressions.validate_username("User-Name"))  
        self.assertFalse(regular_expressions.validate_username("user123"))  
        self.assertTrue(regular_expressions.validate_username("A P")) 



class TestFreeContextGrammar(unittest.TestCase):

    def test_standard_cases(self):
        valid_input = ["beginning", "saludaralforastero", "preguntarsinecesitaayuda", "darcomida"]
        self.assertTrue(context_free_grammar.validateachievement(valid_input))

    def test_limit_cases(self):
        invalid_input = ["saludaralforastero", "mantenerdistancia", "salvarforasterodezombies"]
        self.assertFalse(context_free_grammar.validateachievement(invalid_input))

        invalid_input2 = ["befinning","saludaralforastero", "preguntarsinecesitaayuda", "darcomida"]
        self.assertFalse(context_free_grammar.validateachievement(invalid_input2))

    def test_interesting_cases(self):
        valid_input_2 = ["beginning", "mantenerdistancia", "salvarforasterodezombies"]
        self.assertTrue(context_free_grammar.validateachievement(valid_input_2))
        





class TestNondeterministicFiniteAutomaton(unittest.TestCase):


    def test_standard_cases(self):
        nfa = non_deterministic_automata.nfa
        self.assertTrue(nfa.accepts("0011010"))
        self.assertTrue(nfa.accepts("0011110000"))
        self.assertTrue(nfa.accepts("001111110"))


    def test_limit_cases(self):
        nfa = non_deterministic_automata.nfa
        self.assertFalse(nfa.accepts("0"))
        self.assertTrue(nfa.accepts("00111010"))
        self.assertFalse(nfa.accepts("00111100001"))

    def test_interesting_cases(self):
        nfa = non_deterministic_automata.nfa
        self.assertFalse(nfa.accepts("00111111"))
        self.assertFalse(nfa.accepts("001111001"))
        self.assertFalse(nfa.accepts("00111100001"))

class TestFiniteStateTransducer(unittest.TestCase):
    
    def test_translates_accept(self):
        
        trans = Transducer()
        
        self.assertTrue(trans.transductorMethod(regular_expressions.validate_username("Juan Perez"), "En el camino se encuentra un zombie, ---- decide esconderse."))
        self.assertTrue(trans.transductorMethod(regular_expressions.validate_username("Juan Duque"), "---- sale de su casa con un bate de beisbol."))
        self.assertTrue(trans.transductorMethod(regular_expressions.validate_username("Gabriel"), "---- empieza a escuchar a un grupo hablar por la radio, pero decide ignorarlos porque podria ser una trampa."))
        
    def test_translates_no_accepts(self):
        
        trans = Transducer()
        
        self.assertFalse(trans.transductorMethod(regular_expressions.validate_username("Alice_Doe"), "En el camino se encuentra un zombie, ---- decide esconderse."))
        self.assertFalse(trans.transductorMethod(regular_expressions.validate_username("user_name 123"), "---- sale de su casa con un bate de beisbol."))
        self.assertFalse(trans.transductorMethod(regular_expressions.validate_username("MarieCurie 9"), "---- empieza a escuchar a un grupo hablar por la radio, pero decide ignorarlos porque podria ser una trampa."))


if __name__ == '__main__':
    unittest.main()
