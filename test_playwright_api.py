import os
import time
from playwright.sync_api import sync_playwright

# Get the exact folder path where this script is running
current_dir = os.path.dirname(os.path.abspath(__file__))
screenshot_path = os.path.join(current_dir, "playwright_home.png")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    print("Navigating to Playwright website...")
    page.goto("https://playwright.dev")
    
    # Save using the absolute, foolproof folder path
    print(f"Saving screenshot to: {screenshot_path}")
    page.screenshot(path=screenshot_path)
    
    time.sleep(2)
    browser.close()
    print("Screenshot Done!")

    # ---------------------------
    # API TEST SECTION
    # ---------------------------
    print("\nRunning API test...")

    # Create a request context (like Postman inside Playwright)
    request_context = p.request.new_context()

    # Simple GET request to a public dummy API
    response = request_context.get("https://jsonplaceholder.typicode.com/posts/1")

    print("Status Code:", response.status)
    print("Response JSON:", response.json())

    # Clean up
    request_context.dispose()
    print("API Test Done!")
