import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose the language: es | en | ru",
                     choices=("es", "en", "ru")
                     )

@pytest.fixture
def browser(request):
    user_language = request.config.getoption("--language")
    #browser_name = request.config.getoption("browser_name")
    #browser = None
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages':user_language})
    browser = webdriver.Chrome(options=options)
    print(f"Browser started with lang opt: {user_language}")
    yield browser

    print("\nquit browser")
    time.sleep(5)
    browser.quit()







    """
    if browser_name == "chrome":
        print("\nstart browser CHROME for test..")
        options = Options()
        options.add_experimental_option('prefs', {'--accept-lang': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart browser FIREFOX for test..")
        options = Options()
        options.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
        """


