from __future__ import annotations
from dataclasses import dataclass
from .exceptions import OperationError

class OperationStrategy:
    name = "op"
    aliases: set[str] = set()
    def execute(self, a: float, b: float) -> float:  # pragma: no cover
        raise NotImplementedError

@dataclass
class Add(OperationStrategy):
    name = "add"
    aliases = {"+","add"}
    def execute(self, a: float, b: float) -> float:
        return a + b

@dataclass
class Sub(OperationStrategy):
    name = "sub"
    aliases = {"-","sub"}
    def execute(self, a: float, b: float) -> float:
        return a - b

@dataclass
class Mul(OperationStrategy):
    name = "mul"
    aliases = {"*","mul"}
    def execute(self, a: float, b: float) -> float:
        return a * b

@dataclass
class Div(OperationStrategy):
    name = "div"
    aliases = {"/","div"}
    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise OperationError("division by zero")
        return a / b

@dataclass
class Pow(OperationStrategy):
    name = "pow"
    aliases = {"^","pow"}
    def execute(self, a: float, b: float) -> float:
        return a ** b

@dataclass
class Root(OperationStrategy):
    name = "root"
    aliases = {"sqrt","root"}
    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise OperationError("0-th root undefined")
        if a < 0 and b % 2 == 0:
            raise OperationError("even root of negative number")
        return a ** (1.0 / b)

_STRATEGIES: list[type[OperationStrategy]] = [Add, Sub, Mul, Div, Pow, Root]

def get_strategy(token: str) -> OperationStrategy:
    t = token.strip().lower()
    for cls in _STRATEGIES:
        if t == cls.name or t in cls.aliases:
            return cls()
    raise OperationError(f"unknown operation '{token}'")
