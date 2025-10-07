from app.calculation import Calculator
from app.history import History
from app.calculator_memento import Caretaker

def test_undo_redo_when_empty():
    c = Calculator(history=History(), caretaker=Caretaker())
    assert c.undo() is False
    assert c.redo() is False
