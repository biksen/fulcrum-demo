from calculator import add

def test_add():
    assert add(2, 3) == 5

def test_add_with_zero_and_negative():
    assert add(0, 0) == 0
    assert add(-2, 5) == 3
