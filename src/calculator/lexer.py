from enum import Enum, auto

# Define TokenType and Token
class TokenType(Enum):
    NUMBER = auto()
    ADD_OP = "+"
    SUB_OP = "-"
    MUL_OP = "*"
    DIV_OP = "/"
    POWER_OP = "^"
    FAC_OP = "!"
    LEFT_PAREN = "("
    RIGHT_PAREN = ")"
    EOF = auto()

class Token:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value

    def __repr__(self):
        return f"Token({self.type}, {repr(self.value)})"

# Lexer class
class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def advance(self):
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def get_number(self):
        result = ''
        while self.current_char is not None and (self.current_char.isdigit() or self.current_char == '.'):
            result += self.current_char
            self.advance()
        return float(result) if '.' in result else int(result)

    def get_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit() or self.current_char == '.':
                return Token(TokenType.NUMBER, self.get_number())

            if self.current_char == '+':
                self.advance()
                return Token(TokenType.ADD_OP, '+')

            if self.current_char == '-':
                self.advance()
                return Token(TokenType.SUB_OP, '-')

            if self.current_char == '*':
                self.advance()
                return Token(TokenType.MUL_OP, '*')

            if self.current_char == '/':
                self.advance()
                return Token(TokenType.DIV_OP, '/')

            if self.current_char == '^':
                self.advance()
                return Token(TokenType.POWER_OP, '^')

            if self.current_char == '!':
                self.advance()
                return Token(TokenType.FAC_OP, '!')

            if self.current_char == '(':
                self.advance()
                return Token(TokenType.LEFT_PAREN, '(')

            if self.current_char == ')':
                self.advance()
                return Token(TokenType.RIGHT_PAREN, ')')

        return Token(TokenType.EOF)

def get_token_list(text):
    lexer = Lexer(text)
    tokens = []
    while True:
        token = lexer.get_token()
        if token.type == TokenType.EOF:
            break
        tokens.append(token)
    return tokens

