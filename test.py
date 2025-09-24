from lexer import Lexer
from parser import Parser

if __name__ == "__main__":
    lxr = Lexer("test.lynx")
    parser = Parser(lxr)
    print(parser.parse())