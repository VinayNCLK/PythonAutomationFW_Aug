
import pytest
from Base.Webdriverfactory import WebdriverFactory

@pytest.yield_fixture()
def setup():
    print("Setup function is called before test method")
    print("Login to app")
    yield
    print("Setup function is called after test method")
    print("Logout from the app")


@pytest.yield_fixture(scope="class")
def onetime_setup(request,browser):
    print("Setup function is called before test Module")
    wdf = WebdriverFactory(browser)
    driver = wdf.getWebdriverInstance()
    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    print("Setup function is called after test Module")
    print("Closing the browser")
    driver.close()


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")
