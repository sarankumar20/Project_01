import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from project_1.Src.Login_page_data import Value

# for failed test case take screenshot
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # file_name = report.nodeid.replace("::", "_") + ".png"
            file_name = "failed_screenshot.png"
            driver.get_screenshot_as_file(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:250px;height:2000px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

@pytest.fixture()
def browser_setup_and_teardown(request):
    global driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(Value.homepage_url)
    request.cls.driver = driver
    yield
    driver.quit()

