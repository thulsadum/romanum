from romanum import to_roman


def test_should_be_i():
    assert to_roman(1) == "I"


def test_should_be_v():
    assert to_roman(5) == "V"


def test_should_be_x():
    assert to_roman(10) == "X"
