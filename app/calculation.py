from __future__ import annotations
from dataclasses import dataclass
from .operations import get_strategy
from .input_validators import parse_operation_line
from .history import History
from .calculator_memento import Memento, Caretaker

@dataclass
class Calculator:
    history: History
    caretaker: Caretaker

    def reset_history(self) -> None:
        self.history.clear()
        self.caretaker.reset()

    def snapshot(self) -> Memento:
        return Memento.from_df(self.history.df.copy())

    def evaluate(self, line: str) -> float:
        self.caretaker.save(self.snapshot())
        op, a, b = parse_operation_line(line)
        strategy = get_strategy(op)
        result = strategy.execute(a, b)
        self.history.add(strategy.name, a, b, result)
        return result

    def undo(self) -> bool:
        m = self.caretaker.undo(self.snapshot())
        if not m:
            return False
        self.history.df = m.to_df()
        return True

    def redo(self) -> bool:
        m = self.caretaker.redo(self.snapshot())
        if not m:
            return False
        self.history.df = m.to_df()
        return True
