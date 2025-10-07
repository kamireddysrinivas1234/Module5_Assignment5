from __future__ import annotations
from typing import Tuple
from .calculator_config import load_config
from .history import History, LoggerObserver, AutoSaveObserver
from .calculation import Calculator
from .calculator_memento import Caretaker
from .exceptions import CalculatorError

USAGE = """\
Commands:
  <op> <a> <b>   perform operation (ops: add/sub/mul/div/pow/root; aliases: + - * / ^ sqrt)
  help           show this help
  history        show history table
  clear          clear history
  undo           undo last change
  redo           redo undone change
  save [path]    save history to CSV (default from config)
  load [path]    load history from CSV (default from config)
  exit | quit    exit the program
"""

def setup() -> Tuple[Calculator, str]:
    cfg = load_config()
    hist = History()
    hist.attach(LoggerObserver(cfg.log_level))
    if cfg.autosave:
        hist.attach(AutoSaveObserver(cfg.history_path))
    hist.load_csv(cfg.history_path)
    calc = Calculator(history=hist, caretaker=Caretaker())
    return calc, cfg.history_path

def process_line(calc: Calculator, default_path: str, line: str) -> str:
    s = line.strip()
    if not s:
        return ""
    cmd, *rest = s.split()
    cmd_low = cmd.lower()
    try:
        if cmd_low in {"help","h","?"}:
            return USAGE
        if cmd_low in {"exit","quit"}:
            return "__EXIT__"
        if cmd_low == "history":
            return str(calc.history.df if not calc.history.df.empty else "No history.")
        if cmd_low == "clear":
            calc.reset_history()
            return "History cleared."
        if cmd_low == "undo":
            return "Undid 1 step(s)." if calc.undo() else "Nothing to undo."
        if cmd_low == "redo":
            return "Redid 1 step(s)." if calc.redo() else "Nothing to redo."
        if cmd_low == "save":
            path = rest[0] if rest else default_path
            calc.history.save_csv(path)
            return f"Saved to {path}"
        if cmd_low == "load":
            path = rest[0] if rest else default_path
            calc.history.load_csv(path)
            calc.caretaker.reset()
            return f"Loaded from {path}"
        result = calc.evaluate(s)
        return str(int(result)) if float(result).is_integer() else str(result)
    except CalculatorError as e:
        return f"Error: {e}"

def repl() -> None:
    print("Enhanced Calculator. Type 'help' for commands.")
    calc, default_path = setup()
    while True:
        try:
            line = input("> ")
        except EOFError:
            print()  # pragma: no cover
            break
        out = process_line(calc, default_path, line)
        if out == "__EXIT__":
            print("Bye!")  # pragma: no cover
            break
        if out:
            print(out)  # pragma: no cover

if __name__ == "__main__":
    repl()  # pragma: no cover
