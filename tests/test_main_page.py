import allure
from pages.main_page import MainPage
import pytest

# Навигация и заголовок
@allure.feature("Main Page")
@allure.story("Header and navigation")
def test_header_and_nav_links(driver):
    page = MainPage(driver)
    page.open()

    with allure.step("Проверяем заголовок на главной странице"):
        header = page.get_header_title()
        # в HTML заголовок — "Marfatech"
        assert header == "Marfatech", f"Ожидали 'Marfatech', получили: '{header}'"

    with allure.step("Проверяем наличие nav ссылок и их href"):
        nav = page.get_nav_links()
        texts = [t for t, _ in nav]
        hrefs = [h for _, h in nav]
        # проверяем пункты меню
        assert "Projects" in texts, f"Отсутствует Projects в {texts}"
        assert "Vacancies" in texts, f"Отсутствует Vacancies в {texts}"
        assert "Contacts" in texts, f"Отсутствует Contacts в {texts}"

        # проверяем окончания ссылок
        assert any(h.endswith("/projects") for h in hrefs), f"Нет ссылки на /projects в {hrefs}"
        assert any(h.endswith("/vacancy") for h in hrefs), f"Нет ссылки на /vacancy в {hrefs}"
        assert any(h.endswith("/contacts") for h in hrefs), f"Нет ссылки на /contacts в {hrefs}"


# Параметризованный тест навигации по шапке
@pytest.mark.parametrize("link_text, expected_path", [
    ("Projects", "/projects"),
    ("Vacancies", "/vacancy"),
    ("Contacts", "/contacts"),
])
@allure.feature("Navigation")
@allure.story("Переход по ссылкам шапки")
def test_navigation_links(driver, link_text, expected_path):
    page = MainPage(driver)
    page.open()

    with allure.step(f"Находим и кликаем по ссылке '{link_text}'"):
        page.click_nav_link_by_text(link_text)

    with allure.step(f"Ждём, пока URL изменится и появится '{expected_path}'"):
        page.wait_for_url_contains(expected_path)

    with allure.step("Проверяем, что текущий URL содержит ожидаемый путь"):
        assert expected_path in driver.current_url, (
            f"Ожидали путь '{expected_path}', но получили '{driver.current_url}'"
        )


# Переход в раздел Contacts
@allure.feature("Navigation")
@allure.story("Переход в раздел Contacts")
def test_open_contacts_and_url(driver):
    page = MainPage(driver)
    page.open()
    with allure.step("Кликаем Contacts и ждём изменения URL"):
        page.go_to_contacts()
        # ждём, что url содержит /contacts
        page.wait_for_url_contains("/contacts")
        assert "/contacts" in driver.current_url.lower()


Проверка полей формы контактов
@allure.feature("Contact form")
@allure.story("Проверка наличия полей формы")
def test_contact_form_fields_present(driver):
    page = MainPage(driver)
    page.open()
    with allure.step("Проверяем, что форма контакта присутствует на странице и содержит поля"):
        assert page.is_contact_form_present(), "Контактная форма или её поля не найдены"

