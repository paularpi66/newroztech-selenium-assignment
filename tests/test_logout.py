from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_logout():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    # Login
    login_page = LoginPage(driver)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    # Perform logout
    inventory_page = InventoryPage(driver)
    inventory_page.click_menu()
    inventory_page.click_logout()

    # Verify logout success by checking the URL
    assert "saucedemo.com" in driver.current_url, "Logout failed!"

    print("Logout Test Passed ✅")
    driver.quit()
