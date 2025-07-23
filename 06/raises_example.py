import pytest

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def test_divide_by_zero():
    with pytest.raises(ValueError) as excinfo:
        divide(10, 0)
    # オプション: 例外メッセージを検証
    assert "Cannot divide by zero" in str(excinfo.value)
