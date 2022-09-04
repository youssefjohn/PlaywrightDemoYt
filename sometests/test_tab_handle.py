from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=2000)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://the-internet.herokuapp.com/windows
    page.goto("https://the-internet.herokuapp.com/windows")

    # Click text=Click Here
    with page.expect_popup() as popup_info:
        page.locator("text=Click Here").click()
    page1 = popup_info.value
    print(page1.locator(".example h3").inner_text())

    with page.expect_popup() as popup_info:
        page.locator("text=Click Here").click()
    page2 = popup_info.value
    print(page2.locator(".example h3").inner_text())
    page.bring_to_front()
    page.wait_for_timeout(2000)
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
