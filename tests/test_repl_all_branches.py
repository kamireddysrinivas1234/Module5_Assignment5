from app.calculator_repl import setup, process_line, USAGE

def test_all_branches(tmp_path):
    calc, default_path = setup()
    p = tmp_path / "h.csv"
    # help variants
    assert USAGE in process_line(calc, str(p), "help")
    assert USAGE in process_line(calc, str(p), "h")
    assert USAGE in process_line(calc, str(p), "?")
    # blank line
    assert process_line(calc, str(p), "   ") == ""
    # history empty
    assert "No history" in process_line(calc, str(p), "history")
    # arithmetic and int/float formatting
    assert process_line(calc, str(p), "+ 2 2") == "4"
    assert process_line(calc, str(p), "div 7 2") == "3.5"
    # undo/redo with content
    assert "Undid 1 step" in process_line(calc, str(p), "undo")
    assert "Redid 1 step" in process_line(calc, str(p), "redo")
    # clear wipes history and stacks
    assert "History cleared." in process_line(calc, str(p), "clear")
    assert "Nothing to undo." in process_line(calc, str(p), "undo")
    assert "Nothing to redo." in process_line(calc, str(p), "redo")
    # save/load (explicit path and default path behavior)
    assert "Saved to" in process_line(calc, str(p), "save " + str(p))
    assert "Loaded from" in process_line(calc, str(p), "load " + str(p))
    assert "Saved to" in process_line(calc, str(p), "save")
    assert "Loaded from" in process_line(calc, str(p), "load")
    # bad op path (error handling)
    out = process_line(calc, str(p), "nope 1 2")
    assert out.startswith("Error:")
