from locators.main_locators import MainLocators as ml


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def get_header(self):
        return self.driver.find_element(*ml.product_header).text
