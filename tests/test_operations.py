import math
import pytest
from app.operations import get_strategy, OperationError

def test_add_and_aliases():
    for token in ["add", "+"]:
        s = get_strategy(token)
        assert s.execute(2, 3) == 5

def test_div_by_zero():
    s = get_strategy("div")
    with pytest.raises(OperationError):
        s.execute(1, 0)

def test_pow_root():
    assert get_strategy("pow").execute(2, 3) == 8
    assert math.isclose(get_strategy("root").execute(27, 3), 3.0)

def test_root_errors():
    with pytest.raises(OperationError):
        get_strategy("root").execute(-8, 2)
    with pytest.raises(OperationError):
        get_strategy("root").execute(8, 0)

def test_unknown():
    with pytest.raises(OperationError):
        get_strategy("???")
