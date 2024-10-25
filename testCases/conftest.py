import pytest
from selenium import webdriver

@pytest.fixture
def setup(browser):
    if browser=="chrome":
        driver=webdriver.Chrome()
        print("Launching Chrome browser........")
    elif browser=="firefox":
        driver=webdriver.Firefox()
        print("Launching Firefox browser........")
    else:
        driver=webdriver.Chrome()
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

# Hook to add extra metadata to the HTML report
def pytest_html_report_title(report):
    report.title = "Truck Parking Club Test Report"

# Hook to add environment info to the HTML report
def pytest_configure(config):
    config._metadata = {
        'Project Name': 'Truck Parking Club',
        'Module Name': 'Login Module',
        'Tester': 'Kapil'
    }

# Hook to remove certain default metadata fields
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
