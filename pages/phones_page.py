import random
import time

from selenium.webdriver.common.by import By

from generator.generator import generated_person
from pages.base_page import BasePage


class PhonePage(BasePage):
    IPHONE_LINK = (By.XPATH, '//a[text()="iPhone"]')

    # Reviews

    REVIEWS_LINK = (By.XPATH, '//ul[@class="nav nav-tabs"] /li[2]')
    INPUT_NAME = (By.CSS_SELECTOR, 'input#input-name')
    TEXTAREA = (By.CSS_SELECTOR, 'textarea#input-review')
    RATING_LIST = (
        By.XPATH, '//div[@class="tab-content"]//div[@id="tab-review"]//div[@class="form-group required"][3]/div/input')
    CONTINUE_BUTTON = (By.CSS_SELECTOR, 'button#button-review')
    ALERT_SUCCESS = (By.CSS_SELECTOR, 'div[class="alert alert-success alert-dismissible"]')

    # By iPhone

    QUANTITY = (By.CSS_SELECTOR, 'input#input-quantity')
    ADD_TO_CART = (By.CSS_SELECTOR, 'button#button-cart')
    ALERT_SUCCESS_IPHONE = (By.CSS_SELECTOR, 'div[class="alert alert-success alert-dismissible"]')
    CART = (By.CSS_SELECTOR, 'div#cart button[data-toggle="dropdown"]')
    CHECKOUT_LINK = (By.XPATH, '//p[@class="text-right"]/a[2]')
    UPDATE_BUTTON = (By.CSS_SELECTOR, 'button[data-original-title="Update"]')
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, 'div[class="buttons clearfix"] div.pull-right')
    ALERT_DANGER = (By.CSS_SELECTOR, 'div[class="alert alert-danger alert-dismissible"]')
    REMOVE_BUTTON = (By.CSS_SELECTOR, 'button[data-original-title="Remove"]')
    SHOPPING_CART_EMPTY = (By.CSS_SELECTOR, 'div#content p')

    def choose_rating(self):
        self.element_is_visible(self.IPHONE_LINK).click()
        person = next(generated_person())
        self.element_is_visible(self.REVIEWS_LINK).click()
        name = person.first_name
        self.element_is_visible(self.INPUT_NAME).send_keys(name)
        self.element_is_visible(self.TEXTAREA).send_keys(
            'iPhone is a revolutionary new mobile phone that allows you to make a call by simply tapping a name or number in your address book, a favorites list, or a call log.')
        rating = self.elements_are_visible(self.RATING_LIST)
        rating[random.randint(0, 4)].click()
        self.element_is_visible(self.CONTINUE_BUTTON).click()
        alert_text = self.element_is_visible(self.ALERT_SUCCESS).text
        return alert_text

    def buy_iphone(self):
        self.element_is_visible(self.QUANTITY).clear()
        self.element_is_visible(self.QUANTITY).send_keys(random.randint(1, 5))
        self.element_is_visible(self.ADD_TO_CART).click()
        alert_text_success = self.element_is_visible(self.ALERT_SUCCESS_IPHONE).text
        self.element_is_visible(self.CART).click()
        self.element_is_visible(self.CHECKOUT_LINK).click()
        self.element_is_visible(self.UPDATE_BUTTON).click()
        self.element_is_visible(self.CHECKOUT_BUTTON).click()
        alert_text_danger = self.element_is_visible(self.ALERT_DANGER).text
        self.element_is_visible(self.REMOVE_BUTTON).click()
        time.sleep(3)
        shopping_cart = self.element_is_visible(self.SHOPPING_CART_EMPTY).text
        return alert_text_success, alert_text_danger, shopping_cart



