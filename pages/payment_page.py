import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from generator.generator import generated_person
from pages.base_page import BasePage


class PaymentPage(BasePage):
    CART = (By.CSS_SELECTOR, 'div#cart')
    VIEW_CART = (By.XPATH, '//p[@class="text-right"]/a[1]')
    CHECKOUT = (By.XPATH, '//div[@ class="buttons clearfix"]/div[@class="pull-right"]')

    # Checkout

    RADIO_GUEST = (By.CSS_SELECTOR, 'input[value="guest"]')
    CONTINUE_BUTTON = (By.CSS_SELECTOR, 'input#button-account')

    # Person Info

    FIRST_NAME = (By.CSS_SELECTOR, 'div[class="form-group required"] input[id="input-payment-firstname"]')
    LAST_NAME = (By.CSS_SELECTOR, 'input#input-payment-lastname')
    E_MAIL = (By.CSS_SELECTOR, 'input#input-payment-email')
    TEL = (By.CSS_SELECTOR, 'input#input-payment-telephone')
    ADDRESS = (By.CSS_SELECTOR, 'input#input-payment-address-1')
    CITY = (By.CSS_SELECTOR, 'div[class="form-group required"] input[id="input-payment-city"]')
    POST_CODE = (By.CSS_SELECTOR, 'div[class="form-group required"] input[id="input-payment-postcode"]')
    COUNTRIES_LIST = (By.CSS_SELECTOR, 'select#input-payment-country option')
    REGIONS = (By.CSS_SELECTOR, 'select#input-payment-zone ')
    REGIONS_LIST = (By.CSS_SELECTOR, 'div[class="form-group required"] select[id="input-payment-zone"] option')

    # Order

    CONTINUE_BUTTON_GUEST = (By.CSS_SELECTOR, '#collapse-payment-address > div > div.buttons > div')
    TEXT_AREA = (By.CSS_SELECTOR, 'textarea[name="comment"]')
    CONTINUE_BUTTON_CHECKOUT = (By.CSS_SELECTOR, '#collapse-shipping-method > div > div.buttons > div')
    CHECKBOX = (By.CSS_SELECTOR, 'input[name="agree"]')
    BUTTON_INPUT = (By.CSS_SELECTOR, 'input#button-payment-method')
    CONFIRM_ORDER = (By.CSS_SELECTOR, 'div.pull-right input#button-confirm')
    H1 = (By.CSS_SELECTOR, 'div#content h1')

    def payment(self):
        self.element_is_visible(self.CART).click()
        self.element_is_visible(self.VIEW_CART).click()
        self.element_is_visible(self.CHECKOUT).click()
        self.element_is_visible(self.RADIO_GUEST).click()
        self.element_is_visible(self.CONTINUE_BUTTON).click()
        person_info = next(generated_person())
        first_name = person_info.first_name
        last_name = person_info.last_name
        e_mail = person_info.e_mail
        tel = person_info.tel
        address = person_info.address
        city = person_info.city
        post_code = person_info.post_code
        self.element_is_visible(self.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(self.LAST_NAME).send_keys(last_name)
        self.element_is_visible(self.E_MAIL).send_keys(e_mail)
        self.element_is_visible(self.TEL).send_keys(tel)
        self.element_is_visible(self.ADDRESS).send_keys(address)
        self.element_is_visible(self.CITY).send_keys(city)
        self.element_is_visible(self.POST_CODE).send_keys(post_code)
        list_of_countries = self.elements_are_present(self.COUNTRIES_LIST)
        list_of_countries[random.randint(0, 253)].click()
        self.scroll_by(150)
        self.element_is_visible(self.REGIONS).click()
        list_of_regions = self.elements_are_visible(self.REGIONS_LIST)
        time.sleep(3)
        if len(list_of_regions) > 2:
            list_of_regions[random.randint(1, 5)].click()
        else:
            self.element_is_visible(self.CONTINUE_BUTTON_GUEST).click()
        self.element_is_visible(self.CONTINUE_BUTTON_GUEST).click()
        self.element_is_visible(self.TEXT_AREA).send_keys('NO COMMENTS')
        self.element_is_visible(self.CONTINUE_BUTTON_CHECKOUT).click()
        self.element_is_visible(self.CHECKBOX).click()
        self.element_is_visible(self.BUTTON_INPUT).click()
        self.element_is_visible(self.CONFIRM_ORDER).click()
        time.sleep(3)
        text = self.element_is_visible(self.H1).text
        return text
