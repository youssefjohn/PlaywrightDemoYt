import time

from playwright.sync_api import Page


def test_refresh_amazon(page: Page) -> None:
    page.goto("https://www.amazon.in/")
    time.sleep(5)
    page.reload(timeout=0)
    time.sleep(5)

