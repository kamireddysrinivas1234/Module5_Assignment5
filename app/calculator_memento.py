from __future__ import annotations
from dataclasses import dataclass
import pandas as pd

@dataclass
class Memento:
    """Snapshot of history (pandas DataFrame)."""
    state_csv: str
    @staticmethod
    def from_df(df: pd.DataFrame) -> "Memento":
        return Memento(state_csv=df.to_csv(index=False))
    def to_df(self) -> pd.DataFrame:
        from io import StringIO
        return pd.read_csv(StringIO(self.state_csv)) if self.state_csv.strip() else pd.DataFrame(columns=["op","a","b","result"])

class Caretaker:
    def __init__(self):
        self._undo_stack: list[Memento] = []
        self._redo_stack: list[Memento] = []
    def reset(self) -> None:
        self._undo_stack.clear()
        self._redo_stack.clear()
    def save(self, m: Memento) -> None:
        self._undo_stack.append(m)
        self._redo_stack.clear()
    def undo(self, current: Memento) -> Memento | None:
        if not self._undo_stack:
            return None
        self._redo_stack.append(current)
        return self._undo_stack.pop()
    def redo(self, current: Memento) -> Memento | None:
        if not self._redo_stack:
            return None
        self._undo_stack.append(current)
        return self._redo_stack.pop()
    @property
    def undo_depth(self) -> int:  # pragma: no cover
        return len(self._undo_stack)
    @property
    def redo_depth(self) -> int:  # pragma: no cover
        return len(self._redo_stack)
