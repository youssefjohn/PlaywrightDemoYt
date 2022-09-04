from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to http://automationpractice.com/index.php
    page.goto("http://automationpractice.com/index.php")

    # Go to http://automationpractice.com/index.php?controller=authentication&back=my-account
    page.goto("http://automationpractice.com/index.php?controller=authentication&back=my-account")

    # Click text=Email address Password Forgot your password? Sign in >> input[name="email"]
    page.locator("text=Email address Password Forgot your password? Sign in >> input[name=\"email\"]").click()

    # Fill text=Email address Password Forgot your password? Sign in >> input[name="email"]
    page.locator("text=Email address Password Forgot your password? Sign in >> input[name=\"email\"]").fill("sjhhh@h.com")

    # Press Tab
    page.locator("text=Email address Password Forgot your password? Sign in >> input[name=\"email\"]").press("Tab")

    # Fill input[name="passwd"]
    page.locator("input[name=\"passwd\"]").fill("hftrffgg")

    # Click button:has-text("Sign in")
    page.locator("button:has-text(\"Sign in\")").click()
    page.wait_for_url("http://automationpractice.com/index.php?controller=authentication")

    # Click text=Authentication failed.
    error_msg = page.locator("xpath=//div[@class='alert alert-danger']//li")

    expect(error_msg).to_be_visible()


    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
