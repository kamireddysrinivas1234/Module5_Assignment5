import builtins
from app.calculator_repl import repl

def test_repl_exit_and_bye(capsys, monkeypatch):
    seq = iter(['exit'])
    def fake_input(_):
        try:
            return next(seq)
        except StopIteration:
            raise EOFError
    monkeypatch.setattr(builtins, 'input', fake_input)
    repl()
    out = capsys.readouterr().out
    assert "Enhanced Calculator. Type 'help' for commands." in out
    assert "Bye!" in out

def test_repl_eof_only(capsys, monkeypatch):
    monkeypatch.setattr(builtins, 'input', lambda _prompt: (_ for _ in ()).throw(EOFError()))
    repl()
    out = capsys.readouterr().out
    assert "Enhanced Calculator. Type 'help' for commands." in out
