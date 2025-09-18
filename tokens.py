from enum import Enum
from json import dumps

class TokenType(Enum):
    EOF = 'EOF'
    ERRORED_TYPE = 'ERRORED_TYPE'

    INT = 'INT'
    FLOAT = 'FLOAT'
    STRING = 'STRING'
    IDENTIFIER = 'IDENTIFIER'
    KEYWORD = 'KEYWORD'
    BOOL = 'BOOL'

    PLUS = 'PLUS'
    MINUS = 'MINUS'
    MULTIPLY = 'MULTIPLY'
    DIVIDE = 'DIVIDE'
    MODULO = 'MODULO'
    EXPONENT = 'EXPONENT'

    ASSIGN = 'ASSIGN'
    EQUAL = 'EQUAL'
    NOT_EQUAL = 'NOT_EQUAL'
    LESS_THAN = 'LESS_THAN'
    LESS_THAN_OR_EQUAL = 'LESS_THAN_OR_EQUAL'
    GREATER_THAN = 'GREATER_THAN'
    GREATER_THAN_OR_EQUAL = 'GREATER_THAN_OR_EQUAL'

    AND = 'AND'
    OR = 'OR'
    NOT = 'NOT'

    INCREMENT = 'INCREMENT'
    DECREMENT = 'DECREMENT'

    LEFT_PAREN = 'LEFT_PAREN'
    RIGHT_PAREN = 'RIGHT_PAREN'
    LEFT_BRACE = 'LEFT_BRACE'
    RIGHT_BRACE = 'RIGHT_BRACE'
    LEFT_BRACKET = 'LEFT_BRACKET'
    RIGHT_BRACKET = 'RIGHT_BRACKET'
    COMMA = 'COMMA'
    DOT = 'DOT'
    COLON = 'COLON'
    SEMICOLON = 'SEMICOLON'

class Token:
    def __init__(self, type_, value, ln, col):
        self.type = type_
        self.value = value
        self.ln = ln
        self.col = col

    def serialize(self):
        return dumps({
            'type': self.type.value,
            'value': self.value,
            'ln': self.ln,
            'col': self.col
        })
    
    def __repr__(self):
        return str(self.serialize())

class TokenStream:
    def __init__(self, tokens, filepath):
        self.tokens = tokens
        self.pos = -1
        self.filepath = filepath

        self.advance()

    @property
    def current(self):
        if self.pos < 0 or self.pos >= len(self.tokens): return Token(TokenType.EOF, '', -1, -1)
        return self.tokens[self.pos]

    def advance(self):
        if self.pos < len(self.tokens) - 1:
            self.pos += 1

    def peek(self, distance=1):
        if self.pos + distance < len(self.tokens): return self.tokens[self.pos + distance]
        return Token(TokenType.EOF, '', -1, -1)

    def serialize(self):
        return dumps({
            'tokens': [token.serialize() for token in self.tokens],
            'filepath': self.filepath
        })
    
    def __repr__(self):
        return str(self.serialize())