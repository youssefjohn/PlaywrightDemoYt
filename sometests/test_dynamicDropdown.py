from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:

    # Go to https://www.makemytrip.com/
    page.goto("https://www.makemytrip.com/")

    # Click text=Multi City >> span
    page.locator("text=Multi City >> span").click()

    # Click text=FromDEL, Delhi Airport India >> input[type="text"]
    page.locator("text=FromDEL, Delhi Airport India >> input[type=\"text\"]").click()

    # Fill [placeholder="From"]
    page.locator("[placeholder=\"From\"]").fill("del")

    # Click text=Jaipur Airport
    page.locator("text=Jaipur Airport").click()
