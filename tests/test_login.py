from selenium import webdriver
from pages.login_page import LoginPage


def test_login():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    assert "inventory.html" in driver.current_url, "Login failed!"
    driver.quit()

    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)
    login_page.enter_username("wrong_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    assert "https://www.saucedemo.com/" == driver.current_url, "Login should not be succeeded!"
    driver.quit()
