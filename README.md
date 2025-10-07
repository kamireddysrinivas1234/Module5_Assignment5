Enhanced Calculator CLI (Python)

A small, pattern-rich command-line calculator with REPL, undo/redo (Memento), observers (autosave/logging), strategy + factory for operations, and a pandas-backed history.

Setup (Windows + VS Code)
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt

Test
python -m pytest

Run
python -m app.calculator_repl

Commands

Ops: add|+, sub|-, mul|*, div|/, pow|^, root|sqrt

Utility: history, clear, undo, redo, save [path], load [path], help, exit|quit

Note on errors

The CLI prints friendly messages like Error: division by zero rather than Python tracebacks.

CI: 100% Coverage Gate

This repo includes .github/workflows/python-app.yml which runs tests and fails the build if coverage is below 100%.
Locally, pytest.ini also enforces --cov-fail-under=100.