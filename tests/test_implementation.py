from regex_expressions import regular_expressions
from gic import context_free_grammar

import unittest

class TestRegularExpressions(unittest.TestCase):

    def test_valid_username(self):
        self.assertTrue(regular_expressions.validate_username("Alice"))
        self.assertTrue(regular_expressions.validate_username("Bob"))
        self.assertTrue(regular_expressions.validate_username("JohnDoe"))
        self.assertTrue(regular_expressions.validate_username("Juan Esteban"))

    def test_invalid_username(self):
        self.assertFalse(regular_expressions.validate_username("123"))
        self.assertFalse(regular_expressions.validate_username("user_name"))
        self.assertFalse(regular_expressions.validate_username("Alice123"))
        self.assertFalse(regular_expressions.validate_username("Alice_Doe"))
        self.assertFalse(regular_expressions.validate_username("Alice@Doe"))




if __name__ == '__main__':
    unittest.main()
