from locators.checkbox_page_locators import CheckboxPageLocators
from pages.home_page import HomePage


class CheckboxPage(HomePage):
    def click_checkbox1(self):
        self.driver.find_element(*CheckboxPageLocators.CHECKBOX1).click()

    def click_checkbox2(self):
        self.driver.find_element(*CheckboxPageLocators.CHECKBOX2).click()

    def click_checkbox3(self):
        self.driver.find_element(*CheckboxPageLocators.CHECKBOX3).click()

    def text_checkbox(self):
        return self.driver.find_element(*CheckboxPageLocators.TEXT_CHECKBOX).is_dispayed()

    def enabled_checkbox1(self):
        return self.driver.find_element(*CheckboxPageLocators.CHECKBOX1).is_selected()

    def enabled_checkbox2(self):
        return self.driver.find_element(*CheckboxPageLocators.CHECKBOX2).is_selected()

    def enabled_checkbox3(self):
        return self.driver.find_element(*CheckboxPageLocators.CHECKBOX3).is_selected()
