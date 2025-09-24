import json

class ASTNode:
    def to_dict(self):
        result = {"kind": self.__class__.__name__}
        for attr, value in self.__dict__.items():
            result[attr] = self._serialize(value)
        return result

    def _serialize(self, value):
        if isinstance(value, ASTNode):
            return value.to_dict()
        elif isinstance(value, list):
            return [self._serialize(v) for v in value]
        elif hasattr(value, "to_dict") and callable(value.to_dict):
            return value.to_dict()
        elif callable(value):
            return f"<function {value.__name__}>"
        else:
            return value

    def __repr__(self):
        return json.dumps(self.to_dict(), indent=2)

class Program(ASTNode):
    def __init__(self, body):
        self.body = body

class IntegerLiteral(ASTNode):
    def __init__(self, value, ln, col):
        self.ln = ln
        self.col = col
        self.value = value

class FloatLiteral(ASTNode):
    def __init__(self, value, ln, col):
        self.ln = ln
        self.col = col
        self.value = value

class StringLiteral(ASTNode):
    def __init__(self, value, ln, col):
        self.ln = ln
        self.col = col
        self.value = value

class Identifier(ASTNode):
    def __init__(self, name, ln, col):
        self.ln = ln
        self.col = col
        self.name = name

class BooleanLiteral(ASTNode):
    def __init__(self, value, ln, col):
        self.ln = ln
        self.col = col
        self.value = value

class ArrayLiteral(ASTNode):
    def __init__(self, elements, ln, col):
        self.ln = ln
        self.col = col
        self.elements = elements

class BinExp(ASTNode):
    def __init__(self, left, operator, right, ln, col):
        self.ln = ln
        self.col = col
        self.left = left
        self.operator = operator
        self.right = right