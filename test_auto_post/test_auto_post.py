import time

from auto_creating_post.google_page import GooglePage


def test(driver):
    google_page = GooglePage(driver, 'https://www.google.com/?hl=RU')
    google_page.open()
    google_page.auto_creating_post()
    time.sleep(5)