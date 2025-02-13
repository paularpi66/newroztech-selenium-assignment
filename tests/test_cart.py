from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_add_to_cart():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    inventory_page = InventoryPage(driver)

    # Extract the text of the first two product names
    product_names = inventory_page.get_first_two_product_names()

    inventory_page.add_items_to_cart()
    inventory_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_items = cart_page.get_cart_items()

    # Check Product count in cart is 2 or not
    assert len(cart_items) == 2, "Cart Item count does not match"
    # Check the Product names in cart are same those were added to the cart
    for item in cart_items:
        assert item.text in product_names, "Add to Cart Failed!"

    cart_page.go_to_inventory_page()
    assert "inventory.html" in driver.current_url, "Failed to Go to Inventory Page from Cart Page!"

    inventory_page.remove_items_from_cart()
    assert inventory_page.get_cart_badge_count() == 0

    inventory_page.add_items_to_cart()
    assert inventory_page.get_cart_badge_count() == 2

    driver.quit()
