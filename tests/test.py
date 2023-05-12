import random
import time

from pages.desktop_page import DesktopPage
from pages.home_page import HomePage


class TestPages:

    def test_desktop_page_search(self, driver):
        desktop_page = DesktopPage(driver, 'https://tutorialsninja.com/demo/index.php?route=product/category&path=20_27')
        desktop_page.open()
        search_result, product,  alert_text = desktop_page.check_search()
        assert search_result == 'Search - iphone', 'Test failed'
        assert product == 'iPhone', 'Test failed'
        assert alert_text.replace("\n", '').replace('×', '') == 'Success: You have added iPhone to your shopping cart!', 'Test failed'

    def test_home_navigation(self, driver):
        sections = ['desktops', 'laptops', 'components', 'tablets', 'software', 'phones', 'cameras', 'mp3']
        home_page = HomePage(driver, 'https://tutorialsninja.com/demo/index.php?route=common/home')
        home_page.open()
        home_page.click_section(sections[random.randint(0, 7)])
        time.sleep(5)

    def test_subsections(self, driver):
        home_page = HomePage(driver, 'https://tutorialsninja.com/demo/index.php?route=common/home')
        home_page.open()
        text = home_page.choose_subsection_components()
        assert text == 'Components', 'Test failed'




