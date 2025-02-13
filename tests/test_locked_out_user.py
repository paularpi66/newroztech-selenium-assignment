from selenium import webdriver
from pages.login_page import LoginPage


def test_locked_out_user():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    # Attempt login with locked-out user
    login_page = LoginPage(driver)
    login_page.enter_username("locked_out_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    # Verify error message
    error_text = login_page.get_error_message()
    assert "Sorry, this user has been locked out." in error_text, "Locked-out test failed!"

    print("Locked-Out User Test Passed ✅")
    driver.quit()
