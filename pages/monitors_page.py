import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from generator.generator import generated_file
from pages.base_page import BasePage


class MonitorsPage(BasePage):
    LIST_VIEW = (By.CSS_SELECTOR, 'button#list-view')
    SELECT_OPTIONS_LIST_SORT = (By.CSS_SELECTOR, 'input-sort')
    SELECT_OPTIONS_LIST_SHOW = (By.CSS_SELECTOR, 'select#input-limit option')
    PRODUCTS_LIST = (By.CSS_SELECTOR, 'div[class="caption"] a')
    # Apple

    APPLE_MONITOR = (By.XPATH, '//a[contains(text(),"Apple")]')
    APPLE_RADIO = (By.CSS_SELECTOR, 'div#input-option218 div input')
    APPLE_CHECKBOX = (By.CSS_SELECTOR, 'div#input-option223 div input')
    APPLE_INPUT_TEXT = (By.CSS_SELECTOR, 'div[class="form-group required"] input#input-option208')
    APPLE_SELECT = (By.CSS_SELECTOR, 'select#input-option217')
    APPLE_TEXT_AREA = (By.CSS_SELECTOR, 'textarea#input-option209')
    APPLE_UPLOAD_FILE = (By.CSS_SELECTOR, 'button#button-upload222')
    APPLE_DATE_BUTTON = (By.CSS_SELECTOR, 'div[class="input-group date"] button[class="btn btn-default"]')
    APPLE_CHOICE_DATE = (By.XPATH, '/html/body/div[4]/div/div[1]/table/tbody/tr/td')
    APPLE_UPLOAD_INPUT = (By.CSS_SELECTOR, 'input#input-option222')
    APPLE_SELECTED_DATE = (By.CSS_SELECTOR, 'div[class="input-group date"] input#input-option219')
    APPLE_TIME_BUTTON = (By.CSS_SELECTOR, 'div[class="input-group time"] button[class="btn btn-default"]')
    APPLE_TIME_VALUE = (By.CSS_SELECTOR, 'input#input-option221')
    # Samsung

    SAMSUNG_MONITOR = (By.XPATH, '//a[contains(text(),"Samsung")]')

    def buy_apple_monitor(self, date):
        self.element_is_visible(self.LIST_VIEW).click()
        self.element_is_visible(self.APPLE_MONITOR).click()
        self.scroll_by(500)
        time.sleep(3)
        radio_list = self.elements_are_visible(self.APPLE_RADIO)
        radio = radio_list[random.randint(0, 1)]
        radio.click()
        checkbox_list = self.elements_are_visible(self.APPLE_CHECKBOX)
        checkbox = checkbox_list[random.randint(0, 3)]
        checkbox.click()
        self.scroll_by(300)
        self.element_is_visible(self.APPLE_INPUT_TEXT).clear()
        self.element_is_visible(self.APPLE_INPUT_TEXT).send_keys('Brand: Apple')
        values = ['1', '2', '3', '4']
        Select(self.driver.find_element(By.CSS_SELECTOR, 'select#input-option217')).select_by_value(
            values[random.randint(0, 3)])
        self.element_is_visible(self.APPLE_TEXT_AREA).send_keys(
            'Support for 2560-by-1600 pixel resolution for display of high definition still and video imagery.')
        self.element_is_visible(self.APPLE_DATE_BUTTON).click()
        dates_list = self.elements_are_visible(self.APPLE_CHOICE_DATE)
        for item in dates_list:
            if item.text == date:
                item.click()
                break
        date = self.element_is_visible(self.APPLE_SELECTED_DATE).get_attribute('value')
        print(f'Selected date {date}')
        element = self.element_is_present(self.APPLE_TIME_VALUE)
        js = self.driver.execute_script("arguments[0].setAttribute('value','00:00')", element)
        self.scroll_by(300)
        time_value = element.get_attribute('value')
        print(f'Selected time {time_value}')






