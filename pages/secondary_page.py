from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep

EXPECTED_URL="/secondary-listings"
FILTER_BTN=(By.CSS_SELECTOR,"div.filter-button")
FOR_SALE_TAG=(By.CSS_SELECTOR,"div.for-sale-tag div[wized='saleTagMLS']")
class SecondaryPage(BasePage):


    def verify_page(self):
        self.verify_partial_url(EXPECTED_URL)

    def filter_button(self):
         sleep(2)
         # self.driver.implicitly_wait(10)
         self.wait_and_click(*FILTER_BTN)
    def get_filtered_products(self):
        self.wait_for_element_visible(*FOR_SALE_TAG)
        tags = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located(FOR_SALE_TAG)
        )
        matching_tags = []
        for tag in tags:
           matching_tags.append(tag)
        return matching_tags
