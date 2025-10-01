from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    SEARCH_INPUT = (By.ID, 'searchInput')
    SEARCH_BUTTON = (By.XPATH, "//button[@type='submit']")
    TH_ALMA_MATER = (By.XPATH, "//table[contains(@class,'infobox')]//tr/th[contains(.,'Alma mater')]")
    TD_ALMA_MATER = (By.XPATH, "//table[contains(@class,'infobox')]//tr/th[contains(.,'Alma mater')]/following-sibling::td")


    def open(self, url):
        self.driver.get(url)

    def search(self, text):
        input_box = self.driver.find_element(*self.SEARCH_INPUT)
        input_box.clear()
        input_box.send_keys(text)
        button = self.driver.find_element(*self.SEARCH_BUTTON)
        button.click()

    def get_alma_mater(self):
        return self.driver.find_element(*self.TD_ALMA_MATER).text