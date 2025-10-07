import pytest
from app.input_validators import parse_operation_line
from app.exceptions import ValidationError

def test_parse_ok():
    op, a, b = parse_operation_line("add 2 3")
    assert op == "add" and a == 2.0 and b == 3.0

@pytest.mark.parametrize("line", ["", "   ", "add 2", "add two three", "add 2 3 4"])
def test_parse_bad(line):
    with pytest.raises(ValidationError):
        parse_operation_line(line)
