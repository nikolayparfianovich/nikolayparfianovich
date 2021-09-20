from Thirgd_Task.Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Thirgd_Task.Config.config import TestData
from Thirgd_Task.Pages.UserPage import UserPage
from Thirgd_Task.Pages.PostersPage import PostersPage


class LoginPage(BasePage):
    USERNAME_FIELD = (By.NAME, 'uname')
    PASSWORD_FIELD = (By.NAME, 'pass')
    LOGIN_BUTTON = (By.XPATH, "//input[@value='login']")
    SIGN_UP_LINK = (By.LINK_TEXT, "signup here")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.maximize_window()
        self.driver.get(TestData.BASE_URL)

    def get_login_page_titile(self, title):
        return self.get_title(title)

    def is_signup_link_exist(self):
        return self.is_visible(self.SIGN_UP_LINK)

    def do_login(self, user_name, password):
        self.do_send_keys(self.USERNAME_FIELD, user_name)
        self.do_send_keys(self.PASSWORD_FIELD, password)
        self.do_click(self.LOGIN_BUTTON)
        return UserPage(self.driver)
