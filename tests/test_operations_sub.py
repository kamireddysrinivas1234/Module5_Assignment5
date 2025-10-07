from app.operations import get_strategy

def test_sub_success():
    assert get_strategy("sub").execute(9, 4) == 5
