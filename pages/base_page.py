from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DEFAULT_TIMEOUT = 10

class BasePage:
    def __init__(self, driver, url=""):
        self.driver = driver
        self.url = url

    def open(self):
        if not self.url:
            raise ValueError("URL for the page is not set")
        self.driver.get(self.url)

    def wait_for_presence(self, locator_tuple, timeout=DEFAULT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator_tuple)
        )

    def wait_for_visibility(self, locator_tuple, timeout=DEFAULT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator_tuple)
        )

    def wait_for_clickable(self, locator_tuple, timeout=DEFAULT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator_tuple)
        )

    def click(self, locator_tuple, timeout=DEFAULT_TIMEOUT):
        elem = self.wait_for_clickable(locator_tuple, timeout=timeout)
        elem.click()

    def get_text(self, locator_tuple, timeout=DEFAULT_TIMEOUT):
        elem = self.wait_for_visibility(locator_tuple, timeout=timeout)
        return elem.text.strip()

    def find_all(self, locator_tuple):
        return self.driver.find_elements(*locator_tuple)

    def wait_for_url_contains(self, substring, timeout=DEFAULT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(
            lambda d: substring in d.current_url
        )

