from selenium.webdriver.common.by import By
from pages.base_page import BasePage

SECONDARY_OPTION=(By.CSS_SELECTOR,"a[href='/secondary-listings']")
class SideMenuPage(BasePage):
    def side_menu(self):
        self.wait_and_click(*SECONDARY_OPTION)


