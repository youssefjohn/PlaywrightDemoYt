from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=3000)
    context = browser.new_context(http_credentials={'username': 'admin', 'password': 'admin'})
    page = context.new_page()

    page.goto("https://the-internet.herokuapp.com/digest_auth")
    text = page.locator("#content p").inner_text()
    print(text)
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
