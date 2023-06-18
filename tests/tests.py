from playwright.sync_api import Page, expect
from pages.cart_popup import CartPopup
from pages.login import LoginPage
from pages.main import MainPage


def test_open_cart_with_1_item_no_discount(
        page: Page,
        login_page: LoginPage,
        main_page: MainPage,
        cart_popup: CartPopup) -> None:

    # When: User is authorized and is on the main page
    main_page.initialize()

    # Then: Main mage has correct URL and title
    expect(page).to_have_url(MainPage.URL)
    expect(page).to_have_title("OK-Notes - Магазин блокнотов")\

    # When: User adds 1 item (no discount) to the Cart
    shopping_item = main_page.select_first_shopping_item_no_discount()
    shopping_item.purchase_btn.click()

    # Then: 1 item count is indicated in the Cart
    expect(main_page.cart_items_count).to_have_text("1")

    # When: User clicks on the Cart
    main_page.cart_btn.click()

    # Then: Cart pop-up is displayed with: item name, item price, total price
    cart_item = cart_popup.find_first_item()
    expect(cart_item.title).to_have_text(shopping_item.name)
    expect(cart_item.price).to_contain_text(shopping_item.price)
    expect(cart_popup.cart_total_price).to_have_text(shopping_item.price)

    # When: User clicks "Go to cart" inside the Card pop-up
    # Then: Cart page is opened
    #    BUG: 500 error when click "open cart" from the cart pop-up


def test_open_cart_with_1_item_with_discount(
        page: Page,
        login_page: LoginPage,
        main_page: MainPage,
        cart_popup: CartPopup) -> None:

    # Given: User is authorized and is on the main page
    main_page.initialize()

    # When: User adds 1 item (no discount) to the Cart
    shopping_item = main_page.select_first_shopping_item_with_discount()
    shopping_item.purchase_btn.click()

    # Then: 1 item count is indicated in the Cart
    expect(main_page.cart_items_count).to_have_text("1")

    # When: User clicks on the Cart
    main_page.cart_btn.click()

    # Then: Cart pop-up is displayed with: item name, item price, total price
    cart_item = cart_popup.find_first_item()
    expect(cart_item.title).to_have_text(shopping_item.name)
    expect(cart_item.price).to_contain_text(shopping_item.price)
    expect(cart_popup.cart_total_price).to_have_text(shopping_item.price)

    # When: User clicks "Go to cart" inside the Card pop-up
    # Then: Cart page is opened
    #    BUG: 500 error when click "open cart" from the cart pop-up


def test_open_cart_with_10_different_items(
        page: Page,
        login_page: LoginPage,
        main_page: MainPage,
        cart_popup: CartPopup) -> None:

    # Bug: When 9 items are added to the cart, the cart pop-up can't be opened
    # Bug: Cart total price is incorrect in case multiple items were added to the cart and the first item had a discount

    # Given: User is authorized and is on the main page
    main_page.initialize()

    # When: User adds 10 items to the Cart
    shopping_items = []
    shopping_items_expected_total_price = 0

    for i in [1, 0, 2, 3, 4, 5, 6, 7]:  # temporary solution to bypass the existing bug: first added item should be without a discount
        shopping_item = main_page.select_shopping_item_by_index(i)
        shopping_item.purchase_btn.click()
        shopping_items.append(shopping_item)
        shopping_items_expected_total_price += int(shopping_item.price)

    main_page.navigate_to_the_next_products_page()

    for i in range(2):  # 2 more items on the next page
        shopping_item = main_page.select_shopping_item_by_index(i)
        shopping_item.purchase_btn.click()
        shopping_items.append(shopping_item)
        shopping_items_expected_total_price += int(shopping_item.price)

    # Then: 10 items count is indicated in the Cart
    expect(main_page.cart_items_count).to_have_text("10")

    # When: User clicks on the Cart
    main_page.cart_btn.click()

    # Then: Cart pop-up is displayed with: item name, item price, total price
    for i in range(10):
        expect(cart_popup.find_item_by_index(i).title).to_have_text(shopping_items[i].name)
        expect(cart_popup.find_item_by_index(i).price).to_contain_text(shopping_items[i].price)
    expect(cart_popup.cart_total_price).to_have_text(str(shopping_items_expected_total_price))

    # When: User clicks "Go to cart" inside the Card pop-up
    # Then: Cart page is opened
    #    BUG: 500 error when click "open cart" from the cart pop-up


def test_open_cart_with_8_similar_items_with_discount(
        page: Page,
        login_page: LoginPage,
        main_page: MainPage,
        cart_popup: CartPopup) -> None:

    # Bug: When 9 items are added to the cart, the cart pop-up can't be opened

    number_of_items = 8

    # Given: User is authorized and is on the main page
    main_page.initialize()

    # When: User adds 8 items to the Cart
    shopping_item = main_page.select_first_shopping_item_with_discount()
    for i in range(number_of_items):
        shopping_item.purchase_btn.click()

    # Then: 8 items count is indicated in the Cart
    expect(main_page.cart_items_count).to_have_text(str(number_of_items))

    # When: User clicks on the Cart
    main_page.cart_btn.click()

    # Then: Cart pop-up is displayed with: item name, item price, total price
    expected_total_price = str(int(shopping_item.price)*number_of_items)
    cart_item = cart_popup.find_first_item()
    expect(cart_item.title).to_have_text(shopping_item.name)
    expect(cart_item.price).to_contain_text(expected_total_price)
    expect(cart_popup.cart_total_price).to_have_text(expected_total_price)

    # When: User clicks "Go to cart" inside the Card pop-up
    # Then: Cart page is opened
    #    BUG: 500 error when click "open cart" from the cart pop-up
