
import builtins
import os
from app.calculator_repl import repl

def test_repl_normal_output_branch(tmp_path, capsys, monkeypatch):
    # Force safe config for the REPL run
    monkeypatch.setenv("AUTOSAVE", "false")
    monkeypatch.setenv("HISTORY_PATH", str(tmp_path / "hist.csv"))
    monkeypatch.setenv("LOG_LEVEL", "ERROR")

    # Feed a calculation then EOF to exit via the EOF path,
    # ensuring the "if out: print(out)" branch is covered.
    seq = iter(["add 1 2"])
    def fake_input(_):
        try:
            return next(seq)
        except StopIteration:
            raise EOFError
    monkeypatch.setattr(builtins, "input", fake_input)

    repl()
    out = capsys.readouterr().out
    # Should show banner and the printed result from the normal path
    assert "Enhanced Calculator. Type 'help' for commands." in out
    assert "\n3\n" in out or "\r\n3\r\n" in out
