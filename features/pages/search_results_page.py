from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage


class SearchResultPage(BasePage):
    BUTTON_FOLLOW = (By.XPATH, "//button[@type='button']")

    def get_follow_button_text(self):
        return self.get_text(self.BUTTON_FOLLOW)
