from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from pages.main_page import MainPage
# from pages.header import Header
from pages.signin_page import SigninPage
# from pages.cart_page import CartPage
# from pages.search_results_page import SearchResultsPage
# from pages.terms_and_conditions_page import TermsAndConditionsPage
# from pages.help_page import HelpPage
from pages.side_menu_page import SideMenuPage
from pages.secondary_page import SecondaryPage
from pages.filterpane_page import FilterPanePage
from pages.filter_results_page import FilterResultsPage


class Application:
    def __init__(self, driver):
        self.driver = driver
        self.base_page = BasePage(driver)
        self.main_page = MainPage(driver)

        self.signin_page = SigninPage(driver)
        self.side_menu_page = SideMenuPage(driver)
        self.secondary_page = SecondaryPage(driver)
        self.filterpane_page = FilterPanePage(driver)
        self.filter_results_page = FilterResultsPage(driver)
