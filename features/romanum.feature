Feature: A roman number can be converted to an arabic number.
  As an ancient maths enthusiast
  I want to convert roman number literals to arabic numbers
  So that I can use modern maths on them

  Scenario Template: Roman number to arabic number conversion
    Given a roman number <roman_number>
    When I convert it
    Then it should match arabic numeral <arabic_number>
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