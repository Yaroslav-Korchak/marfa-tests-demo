from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

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
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator_tuple)
            )
        except TimeoutException:
            return None

    def wait_for_visibility(self, locator_tuple, timeout=DEFAULT_TIMEOUT):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator_tuple)
            )
        except TimeoutException:
            return None

    def wait_for_clickable(self, locator_tuple, timeout=DEFAULT_TIMEOUT):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator_tuple)
            )
        except TimeoutException:
            return None

    def click(self, locator_tuple, timeout=DEFAULT_TIMEOUT):
        elem = self.wait_for_clickable(locator_tuple, timeout)
        if elem:
            elem.click()
            return True
        return False

    def get_text(self, locator_tuple, timeout=DEFAULT_TIMEOUT):
        elem = self.wait_for_visibility(locator_tuple, timeout)
        if elem:
            return elem.text.strip()
        return ""

    def find_all(self, locator_tuple):
        return self.driver.find_elements(*locator_tuple)

    def wait_for_url_contains(self, substring, timeout=DEFAULT_TIMEOUT):
        try:
            return WebDriverWait(self.driver, timeout).until(
                lambda d: substring in d.current_url
            )
        except TimeoutException:
            return False