from playwright.sync_api import Page
from pages.objects.cart_item import CartItem


class CartPopup:

    def __init__(self, page: Page) -> None:
        self.page = page

        self.cart_items = page.locator("li.basket-item")
        self.cart_total_price = page.locator("span.basket_price")
        self.go_to_cart_btn = page.get_by_role("button", name="Перейти в корзину")
        self.clear_cart_btn = page.get_by_role("button", name="Очистить корзину")

    def find_first_item(self) -> CartItem:
        locator = self.cart_items.first
        return CartItem(locator)

    def find_item_by_index(self, index: int) -> CartItem:
        locator = self.cart_items.nth(index)
        return CartItem(locator)

