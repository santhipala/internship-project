from time import sleep

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time

SECONDARY_OPTION=(By.CSS_SELECTOR,"a.menu-text-link-leaderboard[href='/secondary-listings']")
class SideMenuPage(BasePage):
    def side_menu(self):
        sleep(2)
        secondary_option=self.wait_for_element_visible(*SECONDARY_OPTION)
        secondary_option.click()


