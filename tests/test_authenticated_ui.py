from playwright.sync_api import sync_playwright

def test_authenticated_dashboard():
    with sync_playwright() as p:
        context = p.chromium.launch().new_context(storage_state="auth/auth.json")
        page = context.new_page()

        page.goto("https://playwright.dev")
        assert "Dashboard" in page.title()

        context.close()
