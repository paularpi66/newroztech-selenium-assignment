from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_for_element(driver, locator, timeout=10):
    """Wait for an element to be visible before interacting with it"""
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))


def wait_for_clickable(driver, locator, timeout=10):
    """Wait for an element to be visible before interacting with it"""
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))


def is_sorted_correctly(values, descending=False):
    """Check if a list is sorted correctly"""
    return values == sorted(values, reverse=descending)

