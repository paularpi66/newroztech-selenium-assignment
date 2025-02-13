from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_cart_badge_count():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    # Login
    login_page = LoginPage(driver)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    # Add items to cart and verify badge count
    inventory_page.add_item_to_cart("backpack")
    assert cart_page.get_cart_badge_count() == 1, "Cart count incorrect after adding backpack"

    inventory_page.add_item_to_cart("bike_light")
    assert cart_page.get_cart_badge_count() == 2, "Cart count incorrect after adding bike light"

    # Remove items and verify badge count
    inventory_page.remove_item_from_cart("backpack")
    assert cart_page.get_cart_badge_count() == 1, "Cart count incorrect after removing backpack"

    inventory_page.remove_item_from_cart("bike_light")
    assert cart_page.get_cart_badge_count() == 0, "Cart count incorrect after removing bike light"

    print("Cart Badge Count Test Passed ✅")
    driver.quit()
