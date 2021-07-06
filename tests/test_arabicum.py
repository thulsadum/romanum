from romanum import to_roman


def test_should_be_i():
    assert to_roman(1) == "I"
