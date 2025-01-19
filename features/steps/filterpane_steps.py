from behave import given, when, then

@when('Filter the products by “want to sell”')
def more_filter(context):
    context.app.filterpane_page.want_to_sell()

@when('Click on Apply Filter')
def apply_filter(context):
    context.app.filterpane_page.apply_filter()