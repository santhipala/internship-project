from time import sleep

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time

SECONDARY_OPTION=(By.CSS_SELECTOR,"a[href='/secondary-listings']")
class SideMenuPage(BasePage):
    def side_menu(self):
        sleep(2)
        self.wait_and_click(*SECONDARY_OPTION)


