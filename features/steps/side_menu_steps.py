from behave import given, when, then


@when('Click on “Secondary” option at the left side menu')
def click_side_menu(context):
    context.app.side_menu_page.side_menu()

