import pytest
import requests
from selenium import webdriver


@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome('/Users/begimaybaiturinova/Downloads/chromedriver')
    driver.implicitly_wait(10)
    yield driver
