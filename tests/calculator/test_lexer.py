import unittest
from calculator.lexer import Lexer, TokenType, Token

class TestLexer(unittest.TestCase):
    def test_get_mul_op(self):
        lexer = Lexer('*')
        self.assertEqual(lexer.get_mul_op(), '*', "Failed to recognize multiplication operator")
        lexer = Lexer('+')
        self.assertIsNone(lexer.get_mul_op(), "Incorrectly recognized multiplication operator")

    def test_get_power_op(self):
        lexer = Lexer('^')
        self.assertEqual(lexer.get_power_op(), '^', "Failed to recognize power operator")
        lexer = Lexer('-')
        self.assertIsNone(lexer.get_power_op(), "Incorrectly recognized power operator")

    def test_get_fac_op(self):
        lexer = Lexer('!')
        self.assertEqual(lexer.get_fac_op(), '!', "Failed to recognize factorial operator")
        lexer = Lexer('/')
        self.assertIsNone(lexer.get_fac_op(), "Incorrectly recognized factorial operator")

    def test_get_left_paren(self):
        lexer = Lexer('(')
        self.assertEqual(lexer.get_left_paren(), '(', "Failed to recognize left parenthesis")
        lexer = Lexer(')')
        self.assertIsNone(lexer.get_left_paren(), "Incorrectly recognized left parenthesis")

    def test_get_right_paren(self):
        lexer = Lexer(')')
        self.assertEqual(lexer.get_right_paren(), ')', "Failed to recognize right parenthesis")
        lexer = Lexer('(')
        self.assertIsNone(lexer.get_right_paren(), "Incorrectly recognized right parenthesis")

if __name__ == '__main__':
    unittest.main()