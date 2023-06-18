import time

from playwright.sync_api import Page

from pages.cart_popup import CartPopup
from pages.objects.shopping_item import ShoppingItem
from pages.login import LoginPage


class MainPage:
    URL = "https://enotes.pointschool.ru/"

    def __init__(self, page: Page) -> None:
        self.page = page
        self.cart_items_count = page.locator(".basket-count-items")
        self.cart_btn = page.locator("id=dropdownBasket")

    def select_first_shopping_item_no_discount(self) -> ShoppingItem:
        locator = self.page.locator(".note-list .note-item:not(.hasDiscount)").nth(0)
        return ShoppingItem(locator)

    def select_first_shopping_item_with_discount(self) -> ShoppingItem:
        locator = self.page.locator(".note-list .note-item.hasDiscount").nth(0)
        return ShoppingItem(locator)

    def select_shopping_item_by_index(self, index: int) -> ShoppingItem:
        locator = self.page.locator(".note-list .note-item.card").nth(index)
        return ShoppingItem(locator)

    def navigate_to_the_next_products_page(self) -> None:
        self.page.locator("li.page-item:not(.active) a.page-link").nth(0).click()
        self.page.wait_for_load_state()
        time.sleep(1)

    def initialize(self):
        login_page = LoginPage(self.page)
        login_page.load()
        login_page.submit_credentials()
        self.page.wait_for_load_state()
        self.cart_items_count.wait_for(timeout=10000, state="visible")

        # clear cart if not empty
        if int(self.cart_items_count.inner_text()) > 0:
            self.cart_btn.click()
            cart_popup = CartPopup(self.page)
            cart_popup.clear_cart_btn.click()
            time.sleep(1)
            assert self.cart_items_count.inner_text() == "0", \
                f"Failed to clear Cart in pre-condition. " \
                f"Expected cart items count to be '0' but found '{self.cart_items_count.inner_text()}'"
