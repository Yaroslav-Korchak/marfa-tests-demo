import pytest
import allure
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager



@pytest.fixture(scope="session", autouse=True)
def check_geo():
    """Пропускаем все тесты, если страна = RU"""
    try:
        resp = requests.get("https://marfa-tech.com/geo.php", timeout=5)
        country = resp.text.strip()
        if country == "RU":
            pytest.skip("❌ Тесты пропущены: страна определена как RU")
    except Exception as e:
        pytest.skip(f"❌ Не удалось получить geo.php: {e}")

@pytest.fixture(scope="function")
def driver():
    options = Options()
    # options.add_argument("--start-maximized")
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Хук для снятия скриншота при падении теста"""
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        try:
            driver = item.funcargs["driver"]
            allure.attach(
                driver.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print("Не удалось сделать скриншот:", e)
