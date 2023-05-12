import time

from pages.desktop_page import DesktopPage


class TestPages:

    def test_desktop_page_search(self, driver):
        desktop_page = DesktopPage(driver, 'https://tutorialsninja.com/demo/index.php?route=product/category&path=20_27')
        desktop_page.open()
        search_result, product,  alert_text = desktop_page.check_search()
        assert search_result == 'Search - iphone', 'Test failed'
        assert product == 'iPhone', 'Test failed'
        assert alert_text.replace("\n", '').replace('×', '') == 'Success: You have added iPhone to your shopping cart!'



