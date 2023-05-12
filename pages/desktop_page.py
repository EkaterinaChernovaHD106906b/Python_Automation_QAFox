import random
import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class DesktopPage(BasePage):
    # search
    SEARCH = (By.CSS_SELECTOR, 'input[name="search"]')
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'span.input-group-btn button[type="button"]')
    SEARCH_RESULT = (By.CSS_SELECTOR, 'div#content h1')
    # product
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div.caption h4')
    # buy
    HREF = (By.CSS_SELECTOR, 'div.caption a')
    QUANTITY = (By.CSS_SELECTOR, 'div#product  input#input-quantity')
    ADD_TO_CARD = (By.CSS_SELECTOR, 'button#button-cart')
    ALERT_SUCCESS = (By.CSS_SELECTOR, 'div[class = "alert alert-success alert-dismissible"]')

    def check_search(self):
        search = self.element_is_visible(self.SEARCH)
        search.send_keys('iphone')
        self.element_is_visible(self.SEARCH_BUTTON).click()
        result = self.element_is_visible(self.SEARCH_RESULT).text
        product = self.element_is_visible(self.PRODUCT_NAME).text
        self.element_is_visible(self.HREF).click()
        self.scroll_by(200)
        input_quantity = self.element_is_clickable(self.QUANTITY)
        input_quantity.click()
        input_quantity.clear()
        input_quantity.send_keys(random.randint(1, 5))
        self.element_is_visible(self.ADD_TO_CARD).click()
        alert_text = self.element_is_visible(self.ALERT_SUCCESS).text
        return result, product, alert_text





