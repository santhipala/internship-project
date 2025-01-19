from behave import given, when, then
from time import sleep


@when('Log in to the page')
def enter_username_password(context):
    context.app.signin_page.enter_username('santhipala@gmail.com')
    context.app.signin_page.enter_password('Qa@25')
    context.app.signin_page.click_signin()
