import random
import time

from selenium.webdriver.common.by import By

from generator.generator import generated_person
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    FIRST_NAME = (By.CSS_SELECTOR, 'input#input-firstname')
    LAST_NAME = (By.CSS_SELECTOR, 'input#input-lastname')
    EMAIL = (By.CSS_SELECTOR, 'input#input-email')
    TEL = (By.CSS_SELECTOR, 'input#input-telephone')
    PASSWORD = (By.CSS_SELECTOR, 'input#input-password')
    PASS_CONFIRM = (By.CSS_SELECTOR, 'input#input-confirm')
    SUBSCRIBE = (By.XPATH, '//div[@class="form-group"]//div//label')
    CHECKBOX = (By.CSS_SELECTOR, 'input[name="agree"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'input[type="submit"]')
    H1 = (By.CSS_SELECTOR, 'div#content h1')

    def registration_new_user(self):
        user = next(generated_person())
        first_name = user.first_name
        last_name = user.last_name
        email = user.e_mail
        tel = user.tel
        password = 'pass'
        self.element_is_visible(self.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(self.LAST_NAME).send_keys(last_name)
        self.element_is_visible(self.EMAIL).send_keys(email)
        self.element_is_visible(self.TEL).send_keys(tel)
        self.element_is_visible(self.PASSWORD).send_keys(password)
        self.element_is_visible(self.PASS_CONFIRM).send_keys(password)
        subscribe = self.elements_are_visible(self.SUBSCRIBE)
        subscribe[random.randint(0, 1)].click()
        self.element_is_visible(self.CHECKBOX).click()
        self.element_is_visible(self.SUBMIT_BUTTON).click()
        time.sleep(3)
        text = self.element_is_visible(self.H1).text
        return text
