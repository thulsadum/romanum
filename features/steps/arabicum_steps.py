from behave import *


# use_step_matcher("re")


@given("an arabic number {arabic_number}")
def step_impl(context, arabic_number):
    """
    :type context: behave.runner.Context
    :type arabic_number: str
    """
    raise NotImplementedError(u'STEP: Given an arabic number <arabic_number>')


@when("I convert it to a roman numeral")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When I convert it to a roman numeral')


@then("it should match the roman numeral {roman_number}")
def step_impl(context, roman_number):
    """
    :type context: behave.runner.Context
    :type roman_number: str
    """
    raise NotImplementedError(u'STEP: Then it should match <roman_number>')
