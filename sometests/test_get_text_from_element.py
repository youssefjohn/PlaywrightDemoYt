from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:

    # Go to https://www.saucedemo.com/
    page.goto("https://www.saucedemo.com/")

    # Click [data-test="login-button"]
    page.locator("[data-test=\"login-button\"]").click()
    text = page.locator("//h3[@data-test='error']").text_content()
    print(text)
    page.locator("#user-name").fill("AutomationNeemo")
    inner_text = page.locator("#user-name").input_value()
    print(inner_text)
    all_cred = page.locator("#login_credentials").all_text_contents()
    print(all_cred)
