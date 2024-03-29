from playwright.sync_api import Playwright, sync_playwright, expect


def test_run(playwright: Playwright) -> None:
    print('running')
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://www.saucedemo.com/
    page.goto("https://www.saucedemo.com/")

    page.locator("#user-name").fill("standard_user", timeout=5000)

    page.locator("#password").fill("secret_sauce")
    # page.pause()

    page.locator("#login-button").click()

    products_header = page.locator("//span[text()='Products']")

    assert products_header.is_visible(), "User is unable to login"
    print('closing')

    # tes
    # burger_menu = page.locator("#react-burger-menu-btn")



    # burger_menu.click()

    # logout_btn = page.locator("//div[@class='bm-menu']//a[text()='Logout']")

    # # page.pause()

    # logout_btn.click()

    # login_btn = page.locator("#login-button")

    # assert login_btn.is_visible(), "Login is not successful"

    # ---------------------
    # context.close()
    # browser.close()

