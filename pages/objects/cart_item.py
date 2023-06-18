from playwright.sync_api import Locator


class CartItem:

    def __init__(self, locator: Locator) -> None:
        self.title = locator.locator(".basket-item-title")
        self.price = locator.locator(".basket-item-price")
