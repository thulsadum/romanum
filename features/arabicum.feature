Feature: An arabic number can be converted to a roman number.
  As an ancient maths enthusiast
  I want to convert arabic numerals to roman numerals
  So that I can present the results of my modern calculations to my ancient colleagues

  Scenario Template: Arabic number to roman number conversion
    Given an arabic number <arabic_number>
    When I convert it to a roman numeral
    Then it should match the roman numeral <roman_number>
    Examples:
      | roman_number | arabic_number |
      | I            | 1             |
      | II           | 2             |
      | IV           | 4             |
      | V            | 5             |
      | IX           | 9             |
      | XLII         | 42            |
      | XCIX         | 99            |
      | MMXIII       | 2013          |
      | MMXXI        | 2021          |
