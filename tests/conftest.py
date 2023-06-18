import pytest
from playwright.sync_api import Page

from pages.login import LoginPage
from pages.main import MainPage
from pages.cart_popup import CartPopup

# note: Fixtures are described here and passed to test class constructors in order to avoid such code
# in test steps: login_page = LoginPage(page)


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)


@pytest.fixture
def main_page(page: Page) -> MainPage:
    return MainPage(page)


@pytest.fixture
def cart_popup(page: Page) -> CartPopup:
    return CartPopup(page)
