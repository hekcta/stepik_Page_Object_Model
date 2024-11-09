import pytest
from selenium import webdriver


def pytest_addoption(parser):
    # parser.addoption('--browser_name', action='store', default=None,
    #                  help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: en or ru")


@pytest.fixture
def browser(request):
    user_language = request.config.getoption("language")
    # browser_name = request.config.getoption("browser_name")
    # browser = None
    # if browser_name == 'chrome':
    #     print("\nЗапуск Chrome браузера для тестирования..")
    #     browser = webdriver.Chrome()
    # elif browser_name == 'firefox':
    #     print("\nЗапуск Firefox браузера для тестирования..")
    #     browser = webdriver.Firefox()
    # else:
    #     raise pytest.UsageError("--browser_name должно быть chrome или firefox")
    # browser.implicitly_wait(150)
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    # options.set_preference("intl.accept_languages", user_language)
    browser = webdriver.Chrome(options=options)

    yield browser
    print("\nЗакрытие браузера..")
    browser.quit()