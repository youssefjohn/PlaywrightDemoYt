from builtins import int

from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:

    # Go to https://selenium08.blogspot.com/2019/11/dropdown.html
    page.goto("https://selenium08.blogspot.com/2019/11/dropdown.html")
    # page.locator("select[name='Month']").select_option(['Sept', 'May', 'July'])
    page.locator("select[name='Month']").select_option(value='Feb', index=6, label='January')
    page.wait_for_timeout(4000)


