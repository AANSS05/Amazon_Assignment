import pytest
from selenium import webdriver
import configparser
config = configparser.ConfigParser()
config.read("..//Utilities//input_properties")

@pytest.fixture(scope= "class")
def setUp(request):
    request.cls.driver = webdriver.Chrome()
    request.cls.driver.get(config.get("Url","base_url"))
    request.cls.driver.maximize_window()
    request.cls.driver.implicitly_wait(20)
    yield
    request.cls.driver.quit()