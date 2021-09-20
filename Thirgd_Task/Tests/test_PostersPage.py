from Thirgd_Task.Tests.test_base import BaseTest
from Thirgd_Task.Pages.PostersPage import PostersPage



class Test_Poster_Page(BaseTest):

    def test_set_comment(self):
        poster_page = PostersPage(self.driver)
        poster_page.go_to_posters_page()
        poster_page.left_comment()
        assert "thank you for your comment." in self.driver.page_source

"""COMMAND FOR RUNNING TESTS : pytest Thirgd_Task/Tests/test_PostersPage.py -v -s  -n 3 --html=./test_posters.html
-n 3 means parralel execution using pytest xdist
--html=./test_posters.html will create basic html report"""