from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=3000)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://demoqa.com/sortable
    page.goto("https://demoqa.com/sortable")

    # Click #demo-tabpane-list >> text=One
    page.locator("//div[@id='demo-tabpane-list']//div[text()='One']").click(button="right")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
