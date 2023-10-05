from regex_expressions import regular_expressions
from gic import context_free_grammar
from automata import automata as non_deterministic_automata
import unittest

class TestRegularExpressions(unittest.TestCase):

    def test_valid_username(self):
        self.assertTrue(regular_expressions.validate_username("Juan Perez"))
        self.assertTrue(regular_expressions.validate_username("Maria Smith"))
        self.assertTrue(regular_expressions.validate_username("John Doe"))

    def test_invalid_username(self):
        self.assertFalse(regular_expressions.validate_username("123"))
        self.assertFalse(regular_expressions.validate_username("user_name 123"))
        self.assertFalse(regular_expressions.validate_username("Alice123 doe"))
        self.assertFalse(regular_expressions.validate_username("Alice_Doe"))
        self.assertFalse(regular_expressions.validate_username("Alice@Doe"))

class TestFreeContextGrammar(unittest.TestCase):

    def test_valid(self):

        valid_input = ["beginning", "saludaralforastero", "preguntarsinecesitaayuda", "darcomida"]
        self.assertTrue(context_free_grammar.validateachievement(valid_input))

        valid_input_2 = ["beginning", "mantenerdistancia", "salvarforasterodezombies"]
        self.assertTrue(context_free_grammar.validateachievement(valid_input_2))

    def test_invalid(self):

        invalid_input = ["saludaralforastero", "mantenerdistancia", "salvarforasterodezombies"]
        self.assertFalse(context_free_grammar.validateachievement(invalid_input))

        invalid_input2 = ["befinning","saludaralforastero", "preguntarsinecesitaayuda", "darcomida"]
        self.assertFalse(context_free_grammar.validateachievement(invalid_input2))

class TestNondeterministicFiniteAutomaton(unittest.TestCase):

    def test_accepts(self):
        
        nfa = non_deterministic_automata.nfa
        self.assertTrue(nfa.accepts("001111110"))
        self.assertTrue(nfa.accepts("00111010"))
        self.assertTrue(nfa.accepts("0011010"))
        self.assertTrue(nfa.accepts("0011110000"))

    def test_no_accepts(self):
        nfa = non_deterministic_automata.nfa

        self.assertFalse(nfa.accepts("0"))
        self.assertFalse(nfa.accepts("00111111"))
        self.assertFalse(nfa.accepts("001111001"))
        self.assertFalse(nfa.accepts("00111100001"))


        
        





if __name__ == '__main__':
    unittest.main()
