from playwright.sync_api import sync_playwright

def test_authenticated_api():
    with sync_playwright() as p:
        request = p.request.new_context(storage_state="auth/auth.json")

        response = request.get("https://playwright.dev/api/user")
        assert response.ok

        print("User API Response:", response.json())
