import random
import time

from pages.desktop_page import DesktopPage
from pages.home_page import HomePage
from pages.monitors_page import MonitorsPage
from pages.mp3players_page import MP3PlayersPage
from pages.payment_page import PaymentPage
from pages.phones_page import PhonePage
from pages.registration_page import RegistrationPage


class TestPages:

    def test_desktop_page_search(self, driver):
        desktop_page = DesktopPage(driver,
                                   'https://tutorialsninja.com/demo/index.php?route=product/category&path=20_27')
        desktop_page.open()
        search_result, product, alert_text = desktop_page.check_search()
        assert search_result == 'Search - iphone', 'Test failed'
        assert product == 'iPhone', 'Test failed'
        assert alert_text.replace("\n", '').replace('×',
                                                    '') == 'Success: You have added iPhone to your shopping cart!', 'Test failed'

    def test_home_navigation(self, driver):
        sections = ['desktops', 'laptops', 'components', 'tablets', 'software', 'phones', 'cameras', 'mp3']
        home_page = HomePage(driver, 'https://tutorialsninja.com/demo/index.php?route=common/home')
        home_page.open()
        home_page.click_section(sections[random.randint(0, 7)])
        time.sleep(5)

    def test_subsections(self, driver):
        home_page = HomePage(driver, 'https://tutorialsninja.com/demo/index.php?route=common/home')
        home_page.open()
        text, text_2 = home_page.choose_subsection_components()
        time.sleep(5)
        print(text_2)
        assert text == 'Components', 'Test failed'
        assert text != text_2

    def test_buy_apple_monitor(self, driver):
        monitors_page = MonitorsPage(driver,
                                     'https://tutorialsninja.com/demo/index.php?route=product/category&path=25_28')
        monitors_page.open()
        text = monitors_page.buy_apple_monitor('14')
        payment_page = PaymentPage(driver,
                                   'https://tutorialsninja.com/demo/index.php?route=product/product&path=25_28&product_id=33')
        payment_page.payment()

        time.sleep(5)
        assert text.replace('×', '').replace('\n',
                                             '') == 'Success: You have added Apple Cinema 30" to your shopping cart!'

    def test_buy_samsung_monitor(self, driver):
        monitors_page = MonitorsPage(driver,
                                     'https://tutorialsninja.com/demo/index.php?route=product/product&path=25_28&product_id=33')
        monitors_page.open()
        text = monitors_page.buy_samsung_monitor()
        payment_page = PaymentPage(driver,
                                   'https://tutorialsninja.com/demo/index.php?route=product/product&path=25_28&product_id=33')
        text_order = payment_page.payment()
        time.sleep(5)
        assert text.replace('×', '').replace('\n',
                                             '') == 'Success: You have added Samsung SyncMaster 941BW to your shopping cart!'
        assert text_order == 'Your order has been placed!'

    def test_phones_page_rating(self, driver):
        phones_page = PhonePage(driver, 'https://tutorialsninja.com/demo/index.php?route=product/category&path=24')
        phones_page.open()
        alert_text = phones_page.choose_rating()
        time.sleep(5)
        assert alert_text == 'Thank you for your review. It has been submitted to the webmaster for approval.'

    def test_buy_iphone(self, driver):
        phones_page = PhonePage(driver,
                                'https://tutorialsninja.com/demo/index.php?route=product/product&path=24&product_id=40')
        phones_page.open()
        alert_text_success, alert_text_danger, shopping_cart = phones_page.buy_iphone()
        time.sleep(5)
        assert alert_text_success.replace('×', '').replace('\n',
                                                           '') == 'Success: You have added iPhone to your shopping cart!'
        assert alert_text_danger.replace('×', '').replace('\n',
                                                          '') == 'Products marked with *** are not available in the desired quantity or not in stock!'
        assert shopping_cart == 'Your shopping cart is empty!'

    def test_add_ipod_to_cart(self, driver):
        mp3players_page = MP3PlayersPage(driver,
                                         'https://tutorialsninja.com/demo/index.php?route=product/category&path=34')
        mp3players_page.open()
        alert_text = mp3players_page.add_to_cart()
        time.sleep(5)
        assert alert_text.replace('×', '').replace('\n', '') == 'Success: You have added iPod Classic to your shopping cart!'

    def test_registration_new_user(self, driver):
        registration_page = RegistrationPage(driver, 'https://tutorialsninja.com/demo/index.php?route=account/register')
        registration_page.open()
        text = registration_page.registration_new_user()
        assert text == 'Your Account Has Been Created!'
