from behave import *

#use_step_matcher("re")
from romanum import from_roman


@given("a roman number {roman_number}")
def step_impl(context, roman_number):
    """
    :type context: behave.runner.Context
    :type roman_number: str
    """
    context.roman_number = roman_number


@when("I convert it")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.result = from_roman(context.roman_number)


@then("it should match arabic numeral {arabic_number:d}")
def step_impl(context, arabic_number):
    """
    :type context: behave.runner.Context
    :type arabic_number: str
    """
    assert context.result == arabic_number
