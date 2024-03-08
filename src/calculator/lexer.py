class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def advance(self):
        """Advance the `pos` and set the `current_char`."""
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None  # Indicates end of input
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        """Skip whitespace characters."""
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def get_mul_op(self):
        """Get a multiplication operator token."""
        if self.current_char == '*':
            self.advance()
            return '*'  # Token for multiplication
        return None

    def get_power_op(self):
        """Get a power operator token."""
        if self.current_char == '^':
            self.advance()
            return '^'  # Token for power
        return None

    def get_fac_op(self):
        """Get a factorial operator token."""
        if self.current_char == '!':
            self.advance()
            return '!'  # Token for factorial
        return None

    def get_left_paren(self):
        """Get a left parenthesis token."""
        if self.current_char == '(':
            self.advance()
            return '('  # Token for left parenthesis
        return None

    def get_right_paren(self):
        """Get a right parenthesis token."""
        if self.current_char == ')':
            self.advance()
            return ')'  # Token for right parenthesis
        return None

    # Include any other methods needed for the lexer
