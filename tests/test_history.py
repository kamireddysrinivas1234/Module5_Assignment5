from app.history import History, LoggerObserver, AutoSaveObserver

def test_history_add_and_clear(tmp_path, capsys):
    h = History()
    h.attach(LoggerObserver("DEBUG"))
    p = tmp_path / "h.csv"
    h.attach(AutoSaveObserver(str(p)))
    h.add("add", 2, 3, 5)
    captured = capsys.readouterr().out
    assert "history rows=1" in captured
    assert p.exists()
    assert len(h.df) == 1
    h.clear()
    assert len(h.df) == 0

def test_load_save(tmp_path):
    h = History()
    p = tmp_path / "x.csv"
    h.add("mul", 2, 4, 8)
    h.save_csv(p)
    h2 = History()
    h2.load_csv(p)
    assert len(h2.df) == 1
    assert list(h2.df.columns) == ["op","a","b","result"]
