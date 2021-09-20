import pytest


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass


class Test_Two(BaseTest):

    @pytest.mark.parametrize("text, result",
                             [('ok', 1), ('ok', 2), ('ok', 3), ('not ok', 'bad1'), ('not ok', 'bad2'),
                              ('not ok', 'bad3')])
    def test_01(self, result, text):
        return result, text
