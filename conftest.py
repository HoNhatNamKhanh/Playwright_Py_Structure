import pytest
import os
from datetime import datetime
from playwright.sync_api import sync_playwright

# ✅ Tự động thêm timestamp vào tên file HTML report
def pytest_configure(config):
    """Tự động tạo thư mục reports/YYYY-MM-DD và file report có giờ-phút-giây"""
    if config.option.htmlpath:
        # 📅 Tạo thư mục theo ngày
        today = datetime.now().strftime("%Y-%m-%d")
        day_folder = os.path.join("reports", today)
        os.makedirs(day_folder, exist_ok=True)

        # 🕒 Tạo timestamp cho file (giờ-phút-giây)
        timestamp = datetime.now().strftime("%H-%M-%S")

        # 📄 Tạo đường dẫn file report đầy đủ
        new_report = os.path.join(day_folder, f"report_{timestamp}.html")

        # Gán lại đường dẫn cho pytest-html
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