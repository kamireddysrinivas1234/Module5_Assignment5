from app.input_validators import parse_operation_line
def test_parse_floats_and_spaces():
    op, a, b = parse_operation_line("  add   2.5   0.5 ")
    assert op == "add" and a == 2.5 and b == 0.5
