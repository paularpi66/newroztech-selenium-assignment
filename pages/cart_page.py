from selenium.webdriver.common.by import By

from utils.common import wait_for_element


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")
        self.cart_items = (By.CLASS_NAME, "inventory_item_name")
        self.continue_shopping = (By.ID, "continue-shopping")
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")

    def get_cart_items(self):
        return self.driver.find_elements(*self.cart_items)

    def click_checkout(self):
        self.driver.find_element(*self.checkout_button).click()

    def go_to_inventory_page(self):
        self.driver.find_element(*self.continue_shopping).click()

    def get_cart_badge_count(self):
        """Retrieve the number of items in the cart badge"""
        try:
            badge = wait_for_element(self.driver, self.cart_badge)
            return int(badge.text)
        except:
            return 0  # If badge is not found, assume cart is empty
