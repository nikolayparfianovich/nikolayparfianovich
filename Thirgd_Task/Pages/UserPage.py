from selenium.webdriver.common.by import By
from Thirgd_Task.Pages.BasePage import BasePage


class UserPage(BasePage):
    LOGO_IMAGE = (By.XPATH, "//img[@src='images/logo.gif']")
    UPDATE_BUTTON = (By.NAME, "update")

    def __init__(self, driver):
        super().__init__(driver)

    def get_currenth_path(self):
        self.get_current_path()

    def is_image_present(self):
        return self.is_visible(self.LOGO_IMAGE)

    def submit_user_info(self):
        self.do_click(self.UPDATE_BUTTON)
