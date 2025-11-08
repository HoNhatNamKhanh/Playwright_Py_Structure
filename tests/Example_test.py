from playwright.sync_api import Page  # chỉ để hỗ trợ autocomplete (type hint)

def test_google_homepage(page):
    page.goto("https://www.google.com")
    assert "Google" in page.title()

def test_facebook_homepage(page):
    page.goto("https://www.facebook.com")
    assert "Facebook" in page.title()

def test_google_search(page):
    page.goto("https://www.google.com")
    page.fill("textarea[name='q']", "Playwright Python")
    page.keyboard.press("Enter")
    page.wait_for_selector("text=Playwright")
    assert "Playwright" in page.content()