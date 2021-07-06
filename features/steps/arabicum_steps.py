from behave import *


# use_step_matcher("re")
from romanum import to_roman


@given("an arabic number {arabic_number}")
def step_impl(context, arabic_number):
    """
    :type context: behave.runner.Context
    :type arabic_number: str
    """
    context.arabic_number = int(arabic_number)


@when("I convert it to a roman numeral")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.result = to_roman(context.arabic_number)


@then("it should match the roman numeral {roman_number}")
def step_impl(context, roman_number):
    """
    :type context: behave.runner.Context
    :type roman_number: str
    """
    assert context.result == roman_number
