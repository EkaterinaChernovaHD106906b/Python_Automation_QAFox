import random

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):
    # navigation

    DESKTOPS = (By.XPATH, '//a[text()="Desktops"]')
    LAPTOPS_NOTEBOOKS = (By.XPATH, '//a[text()="Laptops & Notebooks"]')
    COMPONENTS = (By.XPATH, '//a[text()="Components"]')
    TABLETS = (By.XPATH, '//a[text()="Tablets"]')
    SOFTWARE = (By.XPATH, '//a[text()="Software"]')
    PHONES = (By.XPATH, '//a[text()="Phones & PDAs"]')
    CAMERAS = (By.XPATH, '//a[text()="Cameras"]')
    MP3_PLAYERS = (By.XPATH, '//a[text()="MP3 Players"]')

    # subsections

    COMPONENTS_SUBSECTION = (By.XPATH, '//a[text()="Show AllComponents"]')
    H_COMPONENTS = (By.CSS_SELECTOR, 'div#content h2')

    def click_section(self, section):
        sections = {'desktops': self.DESKTOPS,
                    'laptops': self.LAPTOPS_NOTEBOOKS,
                    'components': self.COMPONENTS,
                    'tablets': self.TABLETS,
                    'software': self.SOFTWARE,
                    'phones': self.PHONES,
                    'cameras': self.CAMERAS,
                    'mp3': self.MP3_PLAYERS
                    }

        self.element_is_visible(sections[section]).click()

    def choose_subsection_components(self):
        self.element_is_visible(self.COMPONENTS).click()
        self.element_is_visible(self.COMPONENTS_SUBSECTION).click()
        text = self.element_is_visible(self.H_COMPONENTS).text
        return text

