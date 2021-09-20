import pytest

@pytest.fixture(params=["chrome", "firefox", "explorit"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        print(request.param)
    if request.param == "firefox":
        print(request.param)
    if request.param == "explorit":
        print(request.param)


