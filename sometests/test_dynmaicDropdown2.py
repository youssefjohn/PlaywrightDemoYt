from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:

    # Go to https://www.cleartrip.com/
    page.goto("https://www.cleartrip.com/")

    trip_mode = page.locator("input[type='radio']")
    print(type(trip_mode))
    print(trip_mode.count())
    trip_mode.nth(1).click()



    # trip_mode.first.check()

    # Click [placeholder="Any worldwide city or airport"] >> nth=0
    page.locator("[placeholder=\"Any worldwide city or airport\"]").first.click()

    # Click text=Mumbai, IN - Chatrapati Shivaji Airport (BOM)
    page.locator("text=Mumbai, IN - Chatrapati Shivaji Airport (BOM)").click()
