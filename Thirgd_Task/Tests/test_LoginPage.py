from Thirgd_Task.Tests.test_base import BaseTest
from Thirgd_Task.Pages.LoginPage import LoginPage
from Thirgd_Task.Config.config import TestData


class TestLogin(BaseTest):

    def test_signup_link_visible(self):
        self.login_page = LoginPage(self.driver)
        flag = self.login_page.is_signup_link_exist()
        assert flag

    def test_login_page_title(self):
        self.login_page = LoginPage(self.driver)
        title = self.login_page.get_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE

    def test_login(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
