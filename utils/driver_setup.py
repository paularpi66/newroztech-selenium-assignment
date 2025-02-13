from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def get_driver():
    """Initialize and return a WebDriver instance"""
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    return driver
