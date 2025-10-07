from app.operations import get_strategy

def test_div_success_alias():
    assert get_strategy('/').execute(6, 3) == 2
