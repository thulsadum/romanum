from romanum import from_roman


def test_should_be_one():
    assert from_roman("I") == 1


def test_should_be_five():
    assert from_roman("V") == 5


def test_should_be_ten():
    assert from_roman("X") == 10


def test_should_be_fifty():
    assert from_roman("L") == 50


def test_should_be_hundred():
    assert from_roman("C") == 100


def test_should_be_500():
    assert from_roman("D") == 500


def test_should_be_1000():
    assert from_roman("M") == 1000


def test_should_be_two():
    assert from_roman("II") == 2


def test_should_be_three():
    assert from_roman("III") == 3


def test_should_be_four():
    assert from_roman("IV") == 4
