import pytest
from selenium import webdriver

import time


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en")


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    time.sleep(2)
    browser.quit()