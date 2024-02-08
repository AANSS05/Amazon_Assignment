# import pytest
# from selenium import webdriver
#
# from Utilities import ReadConfigurations
# import pytest
# @pytest.fixture()
# def setup_and_teardown(request):
#     browser = ReadConfigurations.read_configurations("basic info","browser")
#     driver = None
#     if browser.__eq__("chrome"):
#         driver = webdriver.Chrome()
#     if browser.__eq__("firefox"):
#         driver = webdriver.Firefox()
#     if browser.__eq__("edge"):
#         driver = webdriver.Edge()
#     else:
#         print("Provide a valid browser option from chrome/firefox/edge.")
#     app_url = ReadConfigurations.read_configurations("basic info","url")
#     driver.get(app_url)
#     driver.maximize_window()
#     request.cls.driver = driver
#     yield
#     driver.quit()



import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import Service
import configparser
config = configparser.ConfigParser()
config.read("..//Utilities//input_properties")


@pytest.fixture
def setUp(request):
    # service_obj = Service("C:\\Users\\Admin\\PycharmProjects\\pythonProject2\\Driver\\chromedriver.exe")
    request.cls.driver = webdriver.Chrome()
    request.cls.driver.get(config.get("Url","base_url"))
    request.cls.driver.maximize_window()
    request.cls.driver.implicitly_wait(20)
    yield
    request.cls.driver.quit()