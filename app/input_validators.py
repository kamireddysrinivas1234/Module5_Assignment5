from __future__ import annotations
from typing import Tuple
from .exceptions import ValidationError

def parse_operation_line(line: str) -> Tuple[str, float, float]:
    if not isinstance(line, str) or not line.strip():
        raise ValidationError("Empty input")
    parts = line.strip().split()
    if len(parts) != 3:
        raise ValidationError("Expected: <op> <a> <b>")
    op, a_str, b_str = parts[0], parts[1], parts[2]
    try:
        a = float(a_str); b = float(b_str)
    except ValueError as e:
        raise ValidationError("Operands must be numbers") from e
    return op, a, b
