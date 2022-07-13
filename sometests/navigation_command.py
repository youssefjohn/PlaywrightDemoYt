from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=3000)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://www.saucedemo.com/
    page.goto("https://www.google.com/")
    page.locator("text=Gmail").click()
    print(page.url)
    page.go_back()
    print(page.url)
    page.go_forward(wait_until="networkidle")
    print(page.url)



    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
