from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep

EXPECTED_URL="/secondary-listings"
LISTINGS=(By.CSS_SELECTOR,'div.properties-counter.listing')
FILTER_BTN=(By.CSS_SELECTOR,"div.filter-button")

class SecondaryPage(BasePage):


    def verify_page(self):
        self.verify_partial_url(EXPECTED_URL)

    def filter_button(self):
         sleep(2)
         self.wait_for_element_clickable(*FILTER_BTN).click()



