# импорт функции проверки
from playwright.sync_api import expect

# импорт модуля
from pages.login import LoginPage

# тест:
# если введены неверные значения в поля ввода,
# то должно выйти ошибка
def test_void_auth_field(page):
    login_page = LoginPage(page)
    login_page.navigate()                                                           # переход по ссылке на сайт с авторизацией
    login_page.login("", "")                                                        # ввод некорректных данных                                                  # 
    expect(login_page.error).to_have_text("Epic sadface: Username is required")     # проверка корректности текста при ошибке