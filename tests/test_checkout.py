from selenium import webdriver

from pages.checkout_complete_page import CheckoutCompletePage
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_checkout():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    inventory_page = InventoryPage(driver)
    inventory_page.add_items_to_cart()
    inventory_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.click_checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.enter_details("John", "Doe", "12345")
    checkout_page.click_continue()
    checkout_page.click_finish()

    assert "checkout-complete.html" in driver.current_url, "Checkout Failed!"
    complete_page = CheckoutCompletePage(driver)
    thanks_message = complete_page.get_thanks_message()
    assert thanks_message == "Thank you for your order!"

    driver.quit()
