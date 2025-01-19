from behave import given, when, then


@given('Open the main page')
def open_main_page(context):
    context.app.main_page.main_page()