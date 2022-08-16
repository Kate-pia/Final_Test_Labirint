import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def web_browser():
    web_driver = webdriver.Chrome('/chromedriver/chromedriver.exe')
    web_driver.maximize_window()
    yield web_driver

    web_driver.quit()


