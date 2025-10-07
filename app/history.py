from __future__ import annotations
from dataclasses import dataclass, field
from typing import Protocol, List
import pandas as pd
from pathlib import Path

class Observer(Protocol):
    def notify(self, df: pd.DataFrame) -> None: ...

@dataclass
class Subject:
    observers: List[Observer] = field(default_factory=list)
    def attach(self, obs: Observer) -> None:
        if obs not in self.observers:
            self.observers.append(obs)
    def detach(self, obs: Observer) -> None:
        if obs in self.observers:
            self.observers.remove(obs)
    def _broadcast(self, df: pd.DataFrame) -> None:
        for obs in list(self.observers):
            obs.notify(df)

@dataclass
class History(Subject):
    df: pd.DataFrame = field(default_factory=lambda: pd.DataFrame(columns=["op","a","b","result"]))
    def add(self, op: str, a: float, b: float, result: float) -> None:
        self.df.loc[len(self.df)] = [op, float(a), float(b), float(result)]
        self._broadcast(self.df)
    def clear(self) -> None:
        self.df = self.df.iloc[0:0].copy()
        self._broadcast(self.df)
    def load_csv(self, path: str) -> None:
        p = Path(path)
        if p.exists():
            self.df = pd.read_csv(p)
            self.df = self.df["op a b result".split()]
            self._broadcast(self.df)
    def save_csv(self, path: str) -> None:
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        self.df.to_csv(path, index=False)

@dataclass
class LoggerObserver:
    level: str = "INFO"
    def notify(self, df):  # pragma: no cover
        if self.level in {"DEBUG","INFO"}:
            print(f"[{self.level}] history rows={len(df)}")

@dataclass
class AutoSaveObserver:
    path: str
    def notify(self, df):
        df.to_csv(self.path, index=False)
