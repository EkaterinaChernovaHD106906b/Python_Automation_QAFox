import os.path
import random
import time

import requests
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
    APPLE_CHOICE_DATE = (By.XPATH, '/html/body/div[3]/div/div[1]/table/tbody/tr/td')
    APPLE_UPLOAD_INPUT = (By.CSS_SELECTOR, 'input#input-option222')
    APPLE_SELECTED_DATE = (By.CSS_SELECTOR, 'div[class="input-group date"] input#input-option219')
    APPLE_TIME_BUTTON = (By.CSS_SELECTOR, 'div[class="input-group time"] button[class="btn btn-default"]')
    APPLE_TIME_VALUE = (By.CSS_SELECTOR, 'input#input-option221')
    DATE_AND_TIME_VALUE = (By.CSS_SELECTOR, 'input#input-option220')
    QUANTITY = (By.CSS_SELECTOR, 'input#input-quantity')
    BUTTON_ADD_TO_CART = (By.CSS_SELECTOR, 'button#button-cart')
    ALERT_SUCCESS = (By.CSS_SELECTOR, 'div[class="alert alert-success alert-dismissible"]')

    # Samsung

    SAMSUNG_MONITOR = (By.XPATH, '//a[contains(text(),"Samsung")]')
    SAMSUNG_QUANTITY = (By.CSS_SELECTOR, 'input#input-quantity')
    SAMSUNG_ADD_TO_CARD = (By.CSS_SELECTOR, 'button#button-cart')

    # Download image

    IMAGE_LINK = (By.XPATH, '//div[@id="content"]//div[1]//ul[@class="thumbnails"][1]//li[1]//a')

    def buy_apple_monitor(self, date):
        self.element_is_visible(self.LIST_VIEW).click()
        self.element_is_visible(self.APPLE_MONITOR).click()
        self.scroll_by(500)
        time.sleep(3)
        radio_list = self.elements_are_visible(self.APPLE_RADIO)
        radio = radio_list[random.randint(0, 1)]
        radio.click()
        checkbox_list = self.elements_are_visible(self.APPLE_CHECKBOX)
        checkbox = checkbox_list[random.randint(0, 2)]
        checkbox.click()
        self.scroll_by(300)
        self.element_is_visible(self.APPLE_INPUT_TEXT).clear()
        self.element_is_visible(self.APPLE_INPUT_TEXT).send_keys('Brand: Apple')
        values = ['1', '2', '3', '4']
        Select(self.driver.find_element(By.CSS_SELECTOR, 'select#input-option217')).select_by_value(
            values[random.randint(0, 3)])
        self.element_is_visible(self.APPLE_TEXT_AREA).send_keys(
            'Support for 2560-by-1600 pixel resolution for display of high definition still and video imagery.')
        input_file = self.element_is_present(self.APPLE_UPLOAD_INPUT)
        self.driver.execute_script(f"arguments[0].setAttribute('value','2b3c0fe5e7b1c27881b4bd79427818d40402edd4')",
                                   input_file)

        self.element_is_visible(self.APPLE_DATE_BUTTON).click()
        dates_list = self.elements_are_present(self.APPLE_CHOICE_DATE)
        for item in dates_list:
            if item.text == date:
                item.click()
                break
        date = self.element_is_visible(self.APPLE_SELECTED_DATE).get_attribute('value')
        print(f'Selected date {date}')
        time_el = self.element_is_present(self.APPLE_TIME_VALUE)
        self.driver.execute_script(f"arguments[0].setAttribute('value','00:00')", time_el)
        self.scroll_by(300)
        time_value = time_el.get_attribute('value')
        print(f'Selected time {time_value}')
        date_and_time_el = self.element_is_visible(self.DATE_AND_TIME_VALUE)
        self.driver.execute_script(f"arguments[0].setAttribute('value','2011-02-14 00:00')", date_and_time_el)
        date_and_time_value = date_and_time_el.get_attribute('value')
        print(f'Selected date and time {date_and_time_value}')
        self.element_is_visible(self.QUANTITY).clear()
        self.element_is_visible(self.QUANTITY).send_keys(random.randint(1, 5))
        self.element_is_visible(self.BUTTON_ADD_TO_CART).click()
        alert_success = self.element_is_visible(self.ALERT_SUCCESS).text
        return alert_success

    def buy_samsung_monitor(self):
        self.element_is_visible(self.SAMSUNG_QUANTITY).clear()
        self.element_is_visible(self.SAMSUNG_QUANTITY).send_keys(random.randint(1, 5))
        self.element_is_visible(self.SAMSUNG_ADD_TO_CARD).click()
        alert_success = self.element_is_visible(self.ALERT_SUCCESS).text
        return alert_success

    def download_image_monitor(self):
        link = self.element_is_present(self.IMAGE_LINK).get_attribute('href')
        path_name_file = rf'C:\Users\user\PycharmProjects\Python_Automation_QAFox\filetest{random.randint(1, 100)}.jpeg'
        with open(path_name_file, 'wb+') as f:
            f.write(requests.get(link).content)
            check_file = os.path.exists(path_name_file)
            f.close()
        os.remove(path_name_file)
        print(path_name_file)
        return check_file




















