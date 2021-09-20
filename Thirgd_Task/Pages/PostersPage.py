from selenium.webdriver.common.by import By
from Thirgd_Task.Pages.BasePage import BasePage
from Thirgd_Task.Config.config import TestData


class PostersPage(BasePage):

    CATEGORIES_LINK = (By.LINK_TEXT, "categories")
    POSTER_LINK = (By.XPATH, "(//h3)[1]")
    COMMENT_LINK_FIRST_POSTER = (By.XPATH, "(//a[contains(text(),'comment on this picture')])[1]")
    NAME_INPUT = (By.ID, "name")
    COMMENT_INPUT = (By.ID, "comment")
    SUBMIT_BTN = (By.NAME, 'Submit')

    def go_to_posters_page(self):
        self.driver.get(TestData.BASE_URL)
        self.do_click(self.CATEGORIES_LINK)
        self.do_click(self.POSTER_LINK)

    def left_comment(self):
        self.do_click(self.COMMENT_LINK_FIRST_POSTER)
        self.switch_to_next_window()
        self.driver.maximize_window()
        self.do_send_keys(self.NAME_INPUT, 'nick')
        self.do_send_keys(self.COMMENT_INPUT, 'test_comment')
        self.do_click(self.SUBMIT_BTN)


