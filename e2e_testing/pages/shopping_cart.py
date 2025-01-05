# страница корзины
class ShopingCartPage:
    def __init__(self, page):
        self.page = page
        self.inventoty_item = page.locator("[data-test=\"inventory-item\"]")    # поле с товарами
        self.button_checkout = page.locator("[data-test=\"checkout\"]")         # кнопка для начала оформления заказа