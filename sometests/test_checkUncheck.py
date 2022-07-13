import time

from playwright.sync_api import Page


def test_check_checkbox(page: Page) -> None:
    page.goto("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
    page.wait_for_timeout(4000)
    page.locator('label', has_text='Monday').check()
    # page.locator(get_days_locator2("Monday")).check()
    assert page.locator(get_days_locator("Monday")).is_checked()
    page.wait_for_timeout(4000)


def get_days_locator(day):
    return f"//label[text()='{day}']/preceding-sibling::input"


def get_days_locator2(day):
    return f"'label', has_text='{day}'"
