import logging
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from unittest import TestCase

from time import sleep

class TestOpenBrowserSite(TestCase):
    @classmethod
    def setUp(cls) -> None:
        super().setUpClass()
        try:
            # NOTE: Requires "chromedriver" binary to be installed in $PATH
            cls.driver = webdriver.Firefox()
        except:
            super().tearDownClass()
            raise
        
    
    def test_open_browser(self):
        
        self.driver.get("http://localhost:8000")
        # self._test_check_title()
        # self._test_team_link()
        # self._test_aboutus_link()
        self._test_translate_button()
        self._test_translate_keyboard_event()
        
        
    def _test_translate_button(self):
        _translate_input = self.driver.find_element(By.CSS_SELECTOR, "#translation-input")
        _translate_input.send_keys("What is your name?")
        sleep(1)
        
        _button = self.driver.find_element(By.CSS_SELECTOR, "#translate-button")
        _button.click()
        sleep(2)
        
    def _test_translate_keyboard_event(self):
        _translate_input = self.driver.find_element(By.CSS_SELECTOR, "#translation-input")
        _translate_input.clear()
        _translate_input.send_keys("How are you?")
        sleep(1)
        
        _translate_input.send_keys(Keys.CONTROL, Keys.ENTER)
        sleep(2)
        
        
    def _test_check_title(self):
        self.driver.title == 'LTS'
        lts = self.driver.find_element(By.CSS_SELECTOR, "#site > a")
        lts.click()
        sleep(1)
        
        
    def _test_team_link(self):
        _team = self.driver.find_element(By.CSS_SELECTOR, "#nav-left > li:nth-child(2) > a")
        _team.click()
        
        sleep(1)
        # return home
        _home = self.driver.find_element(By.CSS_SELECTOR, "#inner > a")
        _home.click()
        sleep(1)
        
    def _test_aboutus_link(self):
        _team = self.driver.find_element(By.CSS_SELECTOR, "#nav-left > li:nth-child(3) > a")
        _team.click()
        
        sleep(1)
        # return home
        _home = self.driver.find_element(By.CSS_SELECTOR, "#inner > a")
        _home.click()
        sleep(1)
        
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()