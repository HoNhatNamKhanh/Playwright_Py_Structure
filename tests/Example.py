import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com/")
    page.get_by_role("combobox", name="Tìm kiếm").click()
    page.get_by_role("combobox", name="Tìm kiếm").fill("something just like this")

    # ---------------------


with sync_playwright() as playwright:
    run(playwright)
