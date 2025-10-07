from app.calculation import Calculator
from app.history import History
from app.calculator_memento import Caretaker

def make_calc():
    return Calculator(history=History(), caretaker=Caretaker())

def test_evaluate_and_undo_redo():
    c = make_calc()
    r1 = c.evaluate("add 2 3")
    assert r1 == 5
    r2 = c.evaluate("mul 10 4")
    assert r2 == 40
    assert len(c.history.df) == 2
    assert c.undo() is True
    assert len(c.history.df) == 1
    assert c.redo() is True
    assert len(c.history.df) == 2
