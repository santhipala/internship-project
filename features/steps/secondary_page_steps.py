from behave import given, when, then

@then('Verify the right page opens')
def verify_right_page(context):
    context.app.secondary_page.verify_page()

@when('Click on Filter')
def click_filter(context):
    context.app.secondary_page.filter_button()

