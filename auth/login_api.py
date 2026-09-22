import os
from playwright.sync_api import sync_playwright

def create_auth_state():
    print("Creating auth.json for public API...")

    # Determine the absolute path to the auth folder
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    auth_folder = os.path.join(project_root, "auth")
    auth_path = os.path.join(auth_folder, "auth.json")

    print(f"Auth will be saved to: {auth_path}")

    with sync_playwright() as p:
        request = p.request.new_context()

        response = request.get("https://jsonplaceholder.typicode.com/posts/1")
        print("Status Code:", response.status)
        print("Response JSON:", response.json())

        request.storage_state(path=auth_path)

    print("auth.json created successfully!")

if __name__ == "__main__":
    create_auth_state()
