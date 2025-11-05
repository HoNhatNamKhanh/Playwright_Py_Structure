import pytest
from utils.report_utils import create_html_report_path
from playwright.sync_api import sync_playwright

def pytest_configure(config):
    """Tự động tạo thư mục reports/YYYY-MM-DD và file report có giờ-phút-giây"""
    if config.option.htmlpath:
       new_report, day_folder = create_html_report_path()
       config.option.htmlpath = new_report

       print(f"\n📁 Thư mục lưu report: {day_folder}")
       print(f"📄 File report: {new_report}\n")

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
    page.close()