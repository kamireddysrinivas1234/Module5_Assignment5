from app.calculator_memento import Caretaker, Memento
import pandas as pd

def test_depths_properties():
    ct = Caretaker()
    assert ct.undo_depth == 0
    assert ct.redo_depth == 0
    m = Memento.from_df(pd.DataFrame(columns=['op','a','b','result']))
    ct.save(m)
    assert ct.undo_depth == 1
    prev = ct.undo(m)
    assert ct.redo_depth == 1
    _ = ct.redo(prev)
    assert ct.undo_depth == 1
