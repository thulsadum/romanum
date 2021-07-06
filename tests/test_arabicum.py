from romanum import to_roman


def test_should_be_i():
    assert to_roman(1) == "I"


def test_should_be_v():
    assert to_roman(5) == "V"


def test_should_be_x():
    assert to_roman(10) == "X"


def test_should_be_l():
    assert to_roman(50) == "L"


def test_should_be_c():
    assert to_roman(100) == "C"


def test_should_be_d():
    assert to_roman(500) == "D"


def test_should_be_m():
    assert to_roman(1000) == "M"
