from selenium.webdriver.common.by import By


class CheckoutCompletePage:
    def __init__(self, driver):
        self.driver = driver
        self.thanks_message_header = (By.XPATH, "//h2[@class='complete-header']")

    def get_thanks_message(self):
        return self.driver.find_element(*self.thanks_message_header).text
