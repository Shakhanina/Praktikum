# страница авторизации
class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username = page.locator("[data-test=\"username\"]")            # поле ввода username
        self.password = page.locator("[data-test=\"password\"]")            # поле ввода password
        self.login_button = page.locator("[data-test=\"login-button\"]")    # кнопка Login
        self.error = page.locator("[data-test=\"error\"]")                  # поле текста при ошибке

    # функция перехода по ссылке
    def navigate(self) -> None:
        self.page.goto("https://www.saucedemo.com")

    # функция заполнения полей ввода и нажатия кнопки Login
    def login(self, username: str, password: str) -> None:
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()