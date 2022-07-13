from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:

    # Go to https://selenium08.blogspot.com/2019/11/dropdown.html
    page.goto("https://selenium08.blogspot.com/2019/11/dropdown.html")

    # Select AF
    page.locator("select[name='country']").select_option(index=2)
    page.wait_for_timeout(3000)
    page.locator("select[name='country']").select_option("")
    # page.locator("//select[@name='country']").select_option(label="Barbados")
    # page.locator("//select[@name='Month']").select_option(['Jan', 'Feb', 'May'])
    # page.locator("//select[@name='Month']").select_text()
    page.wait_for_timeout(5000)

