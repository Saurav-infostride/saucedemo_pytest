import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture(params=["chrome"],scope='class')
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(ChromeDriverManager().install())
        web_driver.maximize_window()
        web_driver.delete_all_cookies()
    if request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        web_driver.maximize_window()
    request.cls.driver = web_driver
    yield
    web_driver.close()

'''Hook for adding info into an HTML report'''
def pytest_configure(config):
    config._metadata['Project Name'] = 'Sauce Demo'
    config._metadata['Tester'] = 'Saurav'