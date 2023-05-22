import time

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class GooglePage(BasePage):
    # google

    GOOGLE_SEARCH = (By.CSS_SELECTOR, 'textarea#APjFqb')
    BUTTON_SEARCH = (By.XPATH, '//div[5]/center/input[1]')
    IMAGES_LIST = (By.CSS_SELECTOR, 'div[class="xte2qe OXEsB l5X1Ye"] div div div img')
    IMAGE = (By.CSS_SELECTOR, 'img[src="https://s0.rbk.ru/v6_top_pics/media/img/0/68/756627188898680.jpg"]')

    # vk

    PHONE_NUMBER = (By.CSS_SELECTOR, 'input#index_email')
    BUTTON_SUBMIT = (By.CSS_SELECTOR, 'button[type="submit"]')
    PASSWORD = (By.CSS_SELECTOR, 'input[name="password"]')
    POST_FIELD = (By.CSS_SELECTOR, 'div#post_field')
    SEND_POST = (By.CSS_SELECTOR, 'div#submit_post div[class="addpost_button_wrap"]')

    def auto_creating_post(self):
        self.element_is_visible(self.GOOGLE_SEARCH).send_keys('джэймс уэб фото')
        self.element_is_visible(self.BUTTON_SEARCH).click()
        images_list = self.elements_are_present(self.IMAGES_LIST)
        image = images_list[1]
        image.click()
        # image_link = self.element_is_present(self.IMAGE).get_attribute('src')
        # self.driver.get(image_link)
        image_link = image.get_attribute('src')
        self.driver.get(image_link)
        action = ActionChains(self.driver)
        action.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
        # save image
        self.driver.get('https://vk.com/login')
        login = ''
        password = ''
        self.element_is_visible(self.PHONE_NUMBER).send_keys(login)
        self.element_is_visible(self.BUTTON_SUBMIT).click()
        self.element_is_visible(self.PASSWORD).send_keys(password)
        self.element_is_visible(self.BUTTON_SUBMIT).click()
        time.sleep(15)
        self.element_is_visible(self.BUTTON_SUBMIT).click()
        self.scroll_by(1500)
        self.element_is_visible(self.POST_FIELD).click()
        self.element_is_visible(self.POST_FIELD).clear()
        self.element_is_visible(self.POST_FIELD).send_keys('Selenium with Python')
        self.scroll_by(1500)
        action.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")
        self.element_is_clickable(self.SEND_POST).click()




