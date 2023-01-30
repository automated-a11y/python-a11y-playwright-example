from pathlib import Path

import pytest
from playwright.sync_api import Page

from automateda11y.pw.axerunner import AxeRunner
from automateda11y.pw.settings import Settings

from tests.html_report import A11yReport


def root_dir():
    return Path(__file__).parent.parent.__str__()


def json_dir():
    return root_dir() + '/reports'


def html_dir():
    return root_dir() + '/html-reports/'


def test_axe(teardown, page: Page):
    Settings.report_dir = json_dir()
    page.goto("file://" + root_dir() + "/tests/test.html")
    data = AxeRunner(page).set_page_title("Page Title").execute()
    assert len(data.violations) == 2


# This HTML reports will work only if Java command line utility is configured :
# https://github.com/automated-a11y/automated-a11y-reporter
@pytest.fixture
def teardown():
    yield None
    a11y_report = A11yReport(json_dir(), "axe", html_dir())
    stdout, stderr = a11y_report.generate_html_report()

    print("Stdout:")
    print(stdout)
