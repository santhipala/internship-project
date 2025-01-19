from behave import given, when, then

@then('Verify the right page opens')
def verify_right_page(context):
    context.app.secondary_page.verify_page()

@when('Click on Filter')
def click_filter(context):
    context.app.secondary_page.filter_button()



@then('Verify all cards have “for sale” tag')
def verify_filtered_products(context):
    tags= context.app.secondary_page.get_filtered_products()
    expected_status='For sale'

    # Make sure tags is not empty or None
    assert tags is not None and len(tags) > 0, "No filtered products found."

    # Iterate over each tag (WebElement) and verify the status
    for tag in tags:
        actual_status = tag.text.strip()  # Use .text to get the text content of the WebElement
        assert expected_status == actual_status, f"Expected status {expected_status}, but got {actual_status} for product"
        # print(f"Product is correctly marked as 'For sale'")

