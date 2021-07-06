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
    if arabic_number == 1:
        return "I"
    elif arabic_number == 5:
        return "V"
    elif arabic_number == 10:
        return "X"
    elif arabic_number == 50:
        return "L"
    elif arabic_number == 100:
        return "C"
    elif arabic_number == 500:
        return "D"
    elif arabic_number == 1000:
        return "M"
