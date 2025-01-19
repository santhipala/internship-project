from selenium.webdriver.common.by import By
from pages.base_page import BasePage

SECONDARY_OPTION=(By.CSS_SELECTOR,"a[href='/secondary-listings']")
class SideMenuPage(BasePage):
    def side_menu(self):
        # Wait for the "Secondary" option to be clickable (up to 10 seconds)
        secondary= self.wait_for_element_clickable(*SECONDARY_OPTION)
        secondary.click()
