from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.common import is_sorted_correctly


def test_sorting():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    # Login
    login_page = LoginPage(driver)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    inventory_page = InventoryPage(driver)

    # Test sorting by Price (Low to High)
    inventory_page.select_sort_option("lohi")
    assert is_sorted_correctly(inventory_page.get_prices(), descending=False), "Low to High sorting failed"

    # Test sorting by Price (High to Low)
    inventory_page.select_sort_option("hilo")
    assert is_sorted_correctly(inventory_page.get_prices(), descending=True), "High to Low sorting failed"

    # Test sorting by Name (A to Z)
    inventory_page.select_sort_option("az")
    assert is_sorted_correctly(inventory_page.get_names(), descending=False), "A to Z sorting failed"

    # Test sorting by Name (Z to A)
    inventory_page.select_sort_option("za")
    assert is_sorted_correctly(inventory_page.get_names(), descending=True), "Z to A sorting failed"

    print("Sorting Test Passed ✅")
    driver.quit()
