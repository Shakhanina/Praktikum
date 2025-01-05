# страница оформления заказа
class CheckoutPage:
    def __init__(self, page):
        self.page = page
        self.field_firstName = page.locator("[data-test=\"firstName\"]")    # поле ввода имени
        self.field_lastName = page.locator("[data-test=\"lastName\"]")      # поле ввода фамилии
        self.field_email = page.locator("[data-test=\"postalCode\"]")       # поле ввода email
        self.button_continue = page.locator("[data-test=\"continue\"]")     # переход на страницу проверки
        self.error = page.locator("[data-test=\"error\"]")  
    
    # функция заполнения полей ввода информации пользователем
    def enters_data(self, firstName: str, lastName: str, email: str):
        self.field_firstName.fill(firstName)
        self.field_lastName.fill(lastName)
        self.field_email.fill(email)
