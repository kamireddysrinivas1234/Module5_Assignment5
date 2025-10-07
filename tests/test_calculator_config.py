from app.calculator_config import load_config, ConfigError

def test_default_config(monkeypatch):
    for key in ["AUTOSAVE","HISTORY_PATH","LOG_LEVEL"]:
        monkeypatch.delenv(key, raising=False)
    cfg = load_config()
    assert cfg.autosave is True
    assert cfg.history_path.endswith("history.csv")
    assert cfg.log_level == "INFO"

def test_bad_log_level(monkeypatch):
    monkeypatch.setenv("LOG_LEVEL", "NOPE")
    try:
        load_config()
        assert False
    except ConfigError as e:
        assert "Invalid LOG_LEVEL" in str(e)

def test_empty_history_path(monkeypatch):
    monkeypatch.setenv("HISTORY_PATH", "")
    try:
        load_config()
        assert False
    except ConfigError:
        pass
