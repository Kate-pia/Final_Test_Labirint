import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def web_browser():
    web_driver = webdriver.Chrome()
    web_driver.maximize_window()
    yield web_driver

    web_driver.quit()
