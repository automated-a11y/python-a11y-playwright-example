from pathlib import Path

import pytest
from automateda11y.pw.htmlcsrunner import HtmlCsRunner
from automateda11y.pw.settings import Settings
from playwright.sync_api import Page

from tests.html_report import A11yReport


def root_dir():
    return Path(__file__).parent.parent.__str__()


def json_dir():
    return root_dir() + '/reports'


def html_dir():
    return root_dir() + '/html-reports/'


def test_html_cs(teardown, page: Page):
    Settings.report_dir = json_dir()
    page.goto("file://" + root_dir() + "/tests/test.html")
    data = HtmlCsRunner(page).set_standard().set_page_title("Page Title").set_ignore_code([]).execute()
    assert data.errors == 5


# This HTML reports will work only if Java command line utility is configured :
# https://github.com/automated-a11y/automated-a11y-reporter
@pytest.fixture
def teardown():
    yield None
    a11y_report = A11yReport(json_dir(), "htmlcs", html_dir())
    stdout, stderr = a11y_report.generate_html_report()

    print("Stdout:")
    print(stdout)
