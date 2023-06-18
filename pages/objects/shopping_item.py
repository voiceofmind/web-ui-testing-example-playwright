from playwright.sync_api import Locator
import re


class ShoppingItem:

    def __init__(self, locator: Locator) -> None:
        self.name = locator.locator(".product_name").inner_text()
        self.purchase_btn = locator.locator("button.actionBuyProduct")

        price = locator.locator(".product_price").inner_text()
        price_split = price.split()
        self.price = re.sub("[^0-9]", "", price_split[0])
