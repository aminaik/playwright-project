from playwright.sync_api import sync_playwright

def login_and_save_state():
    print("Starting Playwright UI login...")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        print("Navigating to login page...")
        page.goto("https://example.com/login")

        print("Filling username...")
        page.fill("#username", "Ami")  # <-- update selector if needed

        print("Filling password...")
        page.fill("#password", "Password123")  # <-- update selector if needed

        print("Clicking login button...")
        page.click("button[type='submit']")  # <-- update selector if needed

        print("Waiting for post-login page...")
        page.wait_for_load_state("networkidle")

        print("Saving auth.json...")
        context.storage_state(path="auth/auth.json")

        browser.close()

    print("Login complete! Auth state saved.")

if __name__ == "__main__":
    login_and_save_state()
