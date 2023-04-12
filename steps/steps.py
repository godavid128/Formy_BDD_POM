from behave import given, then, when

from pages.home_page import HomePage


@when(u'Logo is displayed')
def step_impl(context):
    print(u'STEP: When Logo is displayed')
    page = HomePage(context.driver)
    assert page.get_logo()


@given(u'Go to the form page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given Go to the form page')


@when(u'I enter first name "Gorodetchi"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter first name "Gorodetchi"')


@when(u'I enter last name "David"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter last name "David"')


@when(u'Click submit')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Click submit')


@then(u'Success message will be displayed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Success message will be displayed')


@when(u'I enter first name "Tarata"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter first name "Tarata"')


@when(u'I enter last name "Andreea"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter last name "Andreea"')


@then(u'I should see "{keyword}"')
def step_impl(context, keyword):
    print(u'STEP: Then I should see "Welcome to Formy"')
    assert keyword in context.driver.page_source
