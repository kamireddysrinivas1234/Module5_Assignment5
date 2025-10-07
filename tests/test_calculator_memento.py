from app.calculator_memento import Memento, Caretaker
import pandas as pd

def test_memento_roundtrip():
    df = pd.DataFrame([["add",2,3,5]], columns=["op","a","b","result"])
    m = Memento.from_df(df)
    df2 = m.to_df()
    assert list(df2.columns) == ["op","a","b","result"]
    assert len(df2) == 1

def test_memento_empty_to_df():
    m = Memento("")
    df = m.to_df()
    assert list(df.columns) == ["op","a","b","result"]
    assert len(df) == 0

def test_caretaker_undo_redo():
    ct = Caretaker()
    m1 = Memento("")
    m2 = Memento("op,a,b,result\nadd,2,3,5\n")
    ct.save(m1); ct.save(m2)
    prev = ct.undo(m2)
    assert isinstance(prev, Memento)
    nxt = ct.redo(prev)
    assert isinstance(nxt, Memento)
