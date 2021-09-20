from Thirgd_Task.Tests.test_base import BaseTest
from Thirgd_Task.Pages.LoginPage import LoginPage
from Thirgd_Task.Config.config import TestData


class Test_User_Page(BaseTest):

    def test_user_page_title(self):
        self.login_page = LoginPage(self.driver)
        user_page = self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        flag = user_page.get_current_path()
        assert flag == TestData.USER_INFO_URI
        user_page.submit_user_info()

    def test_image(self):
        self.login_page = LoginPage(self.driver)
        user_page = self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        user_page.is_image_present()

