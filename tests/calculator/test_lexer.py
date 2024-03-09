import unittest
from calculator.lexer import Lexer, TokenType, Token

class TestLexer(unittest.TestCase):
    def test_number(self):
        lexer = Lexer("123")
        token = lexer.get_token()
        self.assertEqual(token, Token(TokenType.NUMBER, 123))
        
        lexer = Lexer("3.1415")
        token = lexer.get_token()
        self.assertEqual(token, Token(TokenType.NUMBER, 3.1415))

    def test_operators(self):
        operators = {
            '+': TokenType.ADD_OP,
            '-': TokenType.SUB_OP,
            '*': TokenType.MUL_OP,
            '/': TokenType.DIV_OP,
            '^': TokenType.POWER_OP,
            '!': TokenType.FAC_OP,
        }
        for char, tokenType in operators.items():
            with self.subTest(char=char):
                lexer = Lexer(char)
                token = lexer.get_token()
                self.assertEqual(token, Token(tokenType, char))

    def test_parentheses(self):
        lexer = Lexer("(")
        token = lexer.get_token()
        self.assertEqual(token, Token(TokenType.LEFT_PAREN, '('))
        
        lexer = Lexer(")")
        token = lexer.get_token()
        self.assertEqual(token, Token(TokenType.RIGHT_PAREN, ')'))

    def test_expression(self):
        lexer = Lexer("3 + 4.2 * (1 - 2)")
        tokens = [
            Token(TokenType.NUMBER, 3),
            Token(TokenType.ADD_OP, '+'),
            Token(TokenType.NUMBER, 4.2),
            Token(TokenType.MUL_OP, '*'),
            Token(TokenType.LEFT_PAREN, '('),
            Token(TokenType.NUMBER, 1),
            Token(TokenType.SUB_OP, '-'),
            Token(TokenType.NUMBER, 2),
            Token(TokenType.RIGHT_PAREN, ')'),
        ]
        for expected_token in tokens:
            token = lexer.get_token()
            self.assertEqual(token, expected_token)
        
        # EOF Token
        token = lexer.get_token()
        self.assertEqual(token, Token(TokenType.EOF))

if __name__ == "__main__":
    unittest.main()

