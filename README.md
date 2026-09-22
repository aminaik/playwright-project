# Authentication Setup

## 1. UI Login
Run:
    python auth/login_ui.py

This generates auth/auth.json containing cookies and tokens.

## 2. API Login (Optional)
Run:
    python auth/login_api.py

## 3. Running Authenticated Tests
Playwright will automatically use auth/auth.json:
    pytest tests/test_authenticated_ui.py
    pytest tests/test_api_authenticated.py

## Notes
- auth.json should never be committed to Git.
- You can regenerate auth.json anytime by re-running login scripts.
