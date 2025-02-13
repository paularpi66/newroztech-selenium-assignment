from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

from utils.common import wait_for_element, wait_for_clickable


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

        self.inventory_list = (By.CLASS_NAME, "inventory_list")
        self.inventory_item_name = (By.CLASS_NAME, "inventory_item_name")

        self.add_backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.add_bike_light = (By.ID, "add-to-cart-sauce-labs-bike-light")

        self.remove_backpack = (By.ID, "remove-sauce-labs-backpack")
        self.remove_bike_light = (By.ID, "remove-sauce-labs-bike-light")

        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")
        self.cart_badge = (By.XPATH, "//span[@class='shopping_cart_badge']")

        # components for sorting
        self.sort_dropdown = (By.CLASS_NAME, "product_sort_container")
        self.price_elements = (By.CLASS_NAME, "inventory_item_price")
        self.name_elements = (By.CLASS_NAME, "inventory_item_name")

        # components for logout
        self.menu_button = (By.ID, "react-burger-menu-btn")
        self.logout_button = (By.ID, "logout_sidebar_link")

    def get_first_two_product_names(self):
        inventory_list_elements = wait_for_element(self.driver, self.inventory_list)
        # Find all product name elements within the inventory list
        product_name_elements = inventory_list_elements.find_elements(*self.inventory_item_name)

        # Extract the text of the first two product names
        return [element.text for element in product_name_elements[:2]]

    def add_item_to_cart(self, item):
        """Add an item to the cart based on item name"""
        item_dict = {
            "backpack": self.add_backpack,
            "bike_light": self.add_bike_light
        }
        wait_for_clickable(self.driver, item_dict[item]).click()

    def remove_item_from_cart(self, item):
        """Remove an item from the cart based on item name"""
        item_dict = {
            "backpack": self.remove_backpack,
            "bike_light": self.remove_bike_light
        }
        wait_for_clickable(self.driver, item_dict[item]).click()

    def add_items_to_cart(self):
        self.driver.find_element(*self.add_backpack).click()
        self.driver.find_element(*self.add_bike_light).click()

    def remove_items_from_cart(self):
        self.driver.find_element(*self.remove_backpack).click()
        self.driver.find_element(*self.remove_bike_light).click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_icon).click()

    def get_cart_badge_count(self):
        try:
            return int(self.driver.find_element(*self.cart_badge).text)
        except NoSuchElementException:
            return 0

    def select_sort_option(self, value):
        """Select sorting option from dropdown"""
        dropdown = Select(self.driver.find_element(*self.sort_dropdown))
        dropdown.select_by_value(value)

    def get_prices(self):
        """Return list of product prices"""
        elements = self.driver.find_elements(*self.price_elements)
        return [float(e.text.replace("$", "")) for e in elements]

    def get_names(self):
        """Return list of product names"""
        elements = self.driver.find_elements(*self.name_elements)
        return [e.text for e in elements]

    def click_menu(self):
        """Click the menu button"""
        wait_for_clickable(self.driver, self.menu_button).click()

    def click_logout(self):
        """Click the logout button"""
        wait_for_clickable(self.driver, self.logout_button).click()