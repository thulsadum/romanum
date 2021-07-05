
def from_roman(roman_number):
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

