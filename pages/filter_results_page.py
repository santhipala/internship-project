from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep


FOR_SALE_TAG=(By.CSS_SELECTOR,"div.for-sale-tag div[wized='saleTagMLS']")
class FilterResultsPage(BasePage):

    def verify_for_sale_tag(self):
        self.wait_for_element_visible(*FOR_SALE_TAG)
        tags = self.find_elements(*FOR_SALE_TAG)
        expected_status = 'For sale'

        # Make sure tags is not empty or None
        assert tags is not None and len(tags) > 0, "No filtered products found."

        # Iterate over each tag (WebElement) and verify the status
        for tag in tags:
            actual_status = tag.text.strip()
            assert expected_status == actual_status, f"Expected status {expected_status}, but got {actual_status} for product"
            # print(f"Product is correctly marked as 'For sale'")
