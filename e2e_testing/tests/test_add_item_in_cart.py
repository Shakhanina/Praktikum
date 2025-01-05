# импорт модуля проверки для теста
from playwright.sync_api import expect

# испорт модулей
from pages.login import LoginPage
from pages.product import ProductPage
from pages.shopping_cart import ShopingCartPage

# тест
# при успешной авторизации и добавление одного элемента в корзину
# он там будет в единственном экземпляре
def test_add_item_in_card(page):
    login_page = LoginPage(page)
    product_page = ProductPage(page)
    cart_page = ShopingCartPage(page)
    login_page.navigate()                                           # переход на сайт тестировки
    login_page.login("standard_user", "secret_sauce")               # ввод данных пользователя
    product_page.button_add_to_cart_sauce_labs_backpack.click()     # на странице продуктов добавляем рюкзак в корзину
    product_page.button_shopping_cart_link.click()                  # переходим в корзину
    expect(cart_page.inventoty_item).to_have_count(1)               # проверка: количество элементов к корзине = 1
    