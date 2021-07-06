def from_roman(roman_number, last_literal='I'):
    roman_literals = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    if roman_number in roman_literals.keys():
        return roman_literals[roman_number]

    current_literal = roman_number[:1]
    next_literal = roman_number[1:2]
    rest = roman_number[1:]

    if from_roman(next_literal) <= from_roman(current_literal):
        return from_roman(current_literal) + from_roman(rest)
    else:
        return -from_roman(current_literal) + from_roman(rest)


def to_roman(arabic_number):
    literal_basis = {
        1: "I",
        5: "V",
        10: "X",
        50: "L",
        100: "C",
        500: "D",
        1000: "M",
    }

    if arabic_number in literal_basis.keys():
        return literal_basis[arabic_number]
