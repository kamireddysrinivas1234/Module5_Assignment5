import os
from dataclasses import dataclass
from dotenv import load_dotenv
from .exceptions import ConfigError

@dataclass(frozen=True)
class Config:
    autosave: bool
    history_path: str
    log_level: str

def load_config() -> Config:
    load_dotenv()
    autosave_str = os.getenv("AUTOSAVE", "true").strip().lower()
    autosave = autosave_str in {"1","true","yes","on"}
    history_path = os.getenv("HISTORY_PATH", "history.csv").strip()
    log_level = os.getenv("LOG_LEVEL", "INFO").strip().upper()
    if not history_path:
        raise ConfigError("HISTORY_PATH cannot be empty")
    if log_level not in {"DEBUG","INFO","WARNING","ERROR","CRITICAL"}:
        raise ConfigError(f"Invalid LOG_LEVEL: {log_level}")
    return Config(autosave=autosave, history_path=history_path, log_level=log_level)
