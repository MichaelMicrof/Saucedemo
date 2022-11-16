import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


BASE_URL = 'https://www.saucedemo.com/'


def init_driver_chrome():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1600,1080")
    options.headless = False
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    return driver


def init_driver_firefox():
    options = webdriver.FirefoxOptions()
    options.add_argument("--width=1600")
    options.add_argument("--height=1080")
    options.headless = True
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
    return driver


@pytest.fixture(params=['chrome'], scope='function', autouse=True)
def init_driver(request):
    driver = None
    if request.param == 'chrome':
        driver = init_driver_chrome()
    elif request.param == 'firefox':
        driver = init_driver_firefox()
    else:
        print('Please pass the correct browser name: {}'.format(request.param))
        raise Exception('driver is not found')

    driver.get(BASE_URL)
    request.cls.driver = driver

    yield driver

    driver.quit()
