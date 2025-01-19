import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep

WANT_TO_SELL = (By.XPATH, "(//div[@class='switcher-button']//div[@class='tag-text-filters' and text()='Want to sell'])[1]")
APPLY_FILTER=(By.CSS_SELECTOR,"a.button-filter.w-button")
FOR_SALE_TAG=(By.CSS_SELECTOR,"div.for-sale-tag div[wized='saleTagMLS']")

class FilterPanePage(BasePage):
    def want_to_sell(self):
        # sleep(2)
        # self.wait_for_element_clickable(*WANT_TO_SELL).click()
        # sleep(2)
        self.wait_and_click(*WANT_TO_SELL)

    def apply_filter(self):
        self.wait_and_click(*APPLY_FILTER)
        # sleep(2)
        # self.wait_for_element_clickable(*APPLY_FILTER).click()
        # sleep(2)




