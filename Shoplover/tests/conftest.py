import pytest
from selenium import webdriver
import time
driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="Edge"
    )

@pytest.fixture(scope= "class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "Edge":
        driver = webdriver.Edge(r"F:\pythonProject3\Drivers\msedgedriver.exe")

    elif browser_name == "firefix":
        driver = webdriver.Firefox(r"F:\pythonProject3\Drivers\geckodriver.exe")

    elif browser_name == "Chrome":
        driver = webdriver.Edge(r"F:\pythonProject3\Drivers\chromedriver.exe")
    driver.implicitly_wait(5)
    driver.get("https://shoplover.com/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    time.sleep(3)
    driver.close()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)