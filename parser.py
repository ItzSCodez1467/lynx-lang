from tokens import Token, TokenType, TokenStream
from errors import error
from astNodes import *

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.tokens: TokenStream = lexer.tokenize()


    def expr(self):
        return None # Placeholder for expression parsing

    def factor(self):
        match self.tokens.current.type:
            case TokenType.INT:
                node = IntegerLiteral(self.tokens.current.value, self.tokens.current.ln, self.tokens.current.col)
                self.tokens.advance()
                return node
            case TokenType.FLOAT:
                node = FloatLiteral(self.tokens.current.value, self.tokens.current.ln, self.tokens.current.col)
                self.tokens.advance()
                return node
            case TokenType.STRING:
                node = StringLiteral(self.tokens.current.value, self.tokens.current.ln, self.tokens.current.col)
                self.tokens.advance()
                return node
            case TokenType.BOOL:
                node = BooleanLiteral(self.tokens.current.value, self.tokens.current.ln, self.tokens.current.col)
                self.tokens.advance()
                return node
            case TokenType.ARRAY:
                def extract_values(token_objs):
                    result = []
                    for tok in token_objs:
                        if tok.type == TokenType.ARRAY:
                            result.append(extract_values(tok.value))
                        else:
                            result.append(tok.value)
                    return result

                array_token_objs = self.tokens.current.value
                array_values = extract_values(array_token_objs)
                node = ArrayLiteral(array_values, self.tokens.current.ln, self.tokens.current.col)
                self.tokens.advance()
                return node
            case TokenType.LEFT_PAREN:
                self.tokens.advance()
                node = self.expr()
                if self.tokens.current.type != TokenType.RIGHT_PAREN:
                    error(self.lexer.filepath, self.tokens.current.ln, 'Expected ")"')
                self.tokens.advance()
                return node
            case _:
                error(self.lexer.filepath, self.tokens.current.ln, f'Unexpected token "{self.tokens.__str__()}"')

    def parse_primary(self):
        nodes = []

        while self.tokens.current.type != TokenType.EOF:
            nodes.append(self.factor()) # Placeholder for now
        
        return nodes
    
    def parse(self):
        return Program(self.parse_primary())