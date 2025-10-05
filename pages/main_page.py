from .base_page import BasePage
from locators import main_page_locators as loc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage(BasePage):
    BASE_URL = "https://marfa-tech.com/"

    def __init__(self, driver):
        super().__init__(driver, url=self.BASE_URL)

    # Форма
    def fill_form(self, name, email):
        self.wait_for_presence(loc.FORM_NAME).send_keys(name)
        self.wait_for_presence(loc.FORM_EMAIL).send_keys(email)

    def submit_form(self):
        self.click(loc.FORM_SUBMIT)

    def email_has_invalid_class(self):
        self.wait_for_presence(loc.FORM_EMAIL_INVALID)
        return True

    def email_error_message_is_visible(self):
        self.wait_for_visibility(loc.FORM_EMAIL_ERROR_TEXT)
        return True

    # Навигация
    def get_header_title(self):
        return self.get_text(loc.HEADER_TITLE)

    def get_nav_links(self):
        links = self.find_all(loc.NAV_LINKS)
        return [(link.text.strip(), link.get_attribute("href")) for link in links]

    def go_to_contacts(self):
        self.click(loc.CONTACTS_LINK)

    def click_nav_link_by_text(self, text):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_any_elements_located(loc.NAV_LINKS)
        )

        # Получаем все элементы после того, как они стали видимыми
        links = self.driver.find_elements(*loc.NAV_LINKS)
        for link in links:
            if link.text.strip() == text:
                link.click()
                return

        raise ValueError(f"Ссылка с текстом '{text}' не найдена")

    # Контактная форма
    def is_contact_form_present(self):
        self.wait_for_presence(loc.FORM_CONTACT)
        required_fields = [loc.FORM_NAME, loc.FORM_EMAIL, loc.FORM_SUBMIT]
        return all(self.wait_for_presence(field) for field in required_fields)


