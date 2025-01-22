from behave import then

@then('Verify all cards have “for sale” tag')
def verify_filtered_products(context):
      context.app.filter_results_page.verify_for_sale_tag()

