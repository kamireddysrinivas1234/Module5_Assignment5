from app.operations import get_strategy
def test_aliases_pow_and_sqrt():
    assert get_strategy("^").execute(2, 5) == 32
    assert get_strategy("sqrt").execute(9, 2) == 3
