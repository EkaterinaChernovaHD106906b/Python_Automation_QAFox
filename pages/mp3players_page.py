import random
import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MP3PlayersPage(BasePage):

    # Add to cart
    LIST_VIEW = (By.CSS_SELECTOR, 'button#list-view')
    SORT_BY = (By.CSS_SELECTOR, 'select#input-sort option')
    SHOW = (By.CSS_SELECTOR, 'select#input-limit option')
    iPOD = (By.XPATH, '//a[text()="iPod Classic"]')
    QUANTITY = (By.CSS_SELECTOR, 'input#input-quantity')
    ADD_TO_CART = (By.CSS_SELECTOR, 'button#button-cart')
    ALERT_SUCCESS = (By.CSS_SELECTOR, 'div[class="alert alert-success alert-dismissible"]')

    def add_to_cart(self):
        self.scroll_by(300)
        self.element_is_visible(self.LIST_VIEW).click()
        show = self.elements_are_present(self.SHOW)
        show[random.randint(0, 4)].click()
        self.scroll_by(200)
        self.element_is_visible(self.iPOD).click()
        self.element_is_visible(self.QUANTITY).clear()
        self.element_is_visible(self.QUANTITY).send_keys(random.randint(1, 5))
        self.element_is_visible(self.ADD_TO_CART).click()
        text_alert = self.element_is_visible(self.ALERT_SUCCESS).text
        return text_alert



