# импорт функции для проверки теста
from playwright.sync_api import expect

# импорт модулей
from pages.login import LoginPage
from pages.product import ProductPage
from pages.shopping_cart import ShopingCartPage
from pages.checkout import CheckoutPage

# тест:
# не успешное оформеление заказа
def test_enters_correct_data_to_place_a_order(page):
    login_page = LoginPage(page)
    product_page = ProductPage(page)
    cart_page = ShopingCartPage(page)
    checkout_page = CheckoutPage(page)
    login_page.navigate()                                                                   # переходим на сайт тестировки
    login_page.login("standard_user", "secret_sauce")                                       # вводим данные пользователя
    product_page.button_add_to_cart_sauce_labs_backpack.click()                             # добавляем 1 рюкзак в корзину
    product_page.button_shopping_cart_link.click()                                          # переходим в корзину
    cart_page.button_checkout.click()                                                       # переходим на страницу оформления
    checkout_page.enters_data("", "", "")       # вводим данные для оформления
    expect(checkout_page.error).to_have_text("Error: First Name is required")
    