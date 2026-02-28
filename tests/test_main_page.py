import allure
import pytest
from pages.main_page import MainPage


# ------------------------
# HEADER
# ------------------------

@pytest.mark.smoke
@allure.feature("Main Page")
@allure.story("Header")
def test_header_title(driver):
    page = MainPage(driver)
    page.open()

    with allure.step("Проверяем заголовок главной страницы"):
        header = page.get_header_title()
        assert header == "Marfatech", \
            f"Ожидали 'Marfatech', получили '{header}'"


# ------------------------
# NAVIGATION LINKS (TEXT)
# ------------------------

@pytest.mark.smoke
@pytest.mark.parametrize("expected_text", [
    "Projects",
    "Vacancies",
    "Contacts",
])
@allure.feature("Main Page")
@allure.story("Navigation links text")
def test_nav_links_text_present(driver, expected_text):
    page = MainPage(driver)
    page.open()

    with allure.step("Получаем тексты ссылок навигации"):
        nav = page.get_nav_links()
        texts = [t for t, _ in nav]

    with allure.step(f"Проверяем наличие ссылки '{expected_text}'"):
        assert expected_text in texts, \
            f"Отсутствует '{expected_text}' в {texts}"


# ------------------------
# NAVIGATION LINKS (URL)
# ------------------------

@pytest.mark.smoke
@pytest.mark.parametrize("expected_path", [
    "/projects",
    "/vacancy",
    "/contacts",
])
@allure.feature("Main Page")
@allure.story("Navigation links URL")
def test_nav_links_href(driver, expected_path):
    page = MainPage(driver)
    page.open()

    with allure.step("Получаем ссылки навигации"):
        nav = page.get_nav_links()
        hrefs = [h for _, h in nav]

    with allure.step(f"Проверяем наличие ссылки с окончанием '{expected_path}'"):
        assert any(h.endswith(expected_path) for h in hrefs), \
            f"Нет ссылки на {expected_path} в {hrefs}"


# ------------------------
# NAVIGATION CLICK
# ------------------------

@pytest.mark.smoke
@pytest.mark.parametrize("link_text, expected_path", [
    ("Projects", "/projects"),
    ("Vacancies", "/vacancy"),
    ("Contacts", "/contacts"),
])
@allure.feature("Navigation")
@allure.story("Navigation by clicking header links")
def test_navigation_links(driver, link_text, expected_path):
    page = MainPage(driver)
    page.open()

    with allure.step(f"Кликаем по ссылке '{link_text}'"):
        page.click_nav_link_by_text(link_text)

    with allure.step("Ждём изменения URL"):
        page.wait_for_url_contains(expected_path)

    assert expected_path in driver.current_url, \
        f"Ожидали путь '{expected_path}', получили '{driver.current_url}'"


# ------------------------
# CONTACT FORM
# ------------------------

@pytest.mark.regression
@allure.feature("Contact form")
@allure.story("Contact form fields presence")
def test_contact_form_fields_present(driver):
    page = MainPage(driver)
    page.open()

    with allure.step("Переходим в раздел Contacts"):
        page.go_to_contacts()
        page.wait_for_url_contains("/contacts")

    with allure.step("Проверяем наличие формы контактов"):
        assert page.is_contact_form_present(), \
            "Контактная форма или её поля не найдены"

