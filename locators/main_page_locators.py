from selenium.webdriver.common.by import By

# Навигация
HEADER_TITLE = (By.CSS_SELECTOR, "h1.Header-Title")
NAV_LINKS = (By.CSS_SELECTOR, ".NavList-Links a")
CONTACTS_LINK = (By.CSS_SELECTOR, '.NavList-Links a[href="/contacts"]')
PROJECTS_LINK = (By.CSS_SELECTOR, '.NavList-Links a[href="/projects"]')
VACANCIES_LINK = (By.CSS_SELECTOR, '.NavList-Links a[href="/vacancy"]')

# Форма
FORM_NAME = (By.CSS_SELECTOR, 'form.Form-Form input[name="name"]')
FORM_EMAIL = (By.CSS_SELECTOR, 'form.Form-Form input[name="email"]')
FORM_SUBMIT = (By.CSS_SELECTOR, 'form.Form-Form button[type="submit"]')
FORM_CONTACT = (By.CSS_SELECTOR, "form.Form-Form")

# Ошибки валидации
FORM_EMAIL_INVALID = (By.CSS_SELECTOR, 'form.Form-Form input[name="email"].is-invalid')
FORM_EMAIL_ERROR_TEXT = (By.XPATH, '//span[contains(text(), "Email address required")]')
