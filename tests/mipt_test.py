import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select


def test(driver):
    page = BasePage(driver, 'https://pk.mipt.ru/bachelor/list/')
    page.open()
    Select(driver.find_element(By.XPATH, '//div[@class="entrant-filter"]//div[2]//div[2]/select')).select_by_value('8')
    Select(driver.find_element(By.XPATH, '//div[@class="entrant-filter"]//div[5]//div//select')).select_by_value('1')
    driver.find_element(By.CSS_SELECTOR, 'div[class="filter-block submit-block"]').click()
    time.sleep(5)




