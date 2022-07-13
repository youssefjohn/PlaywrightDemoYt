import time
from playwright.sync_api import Page


def test_refresh1(page: Page) -> None:
    page.goto("https://www.amazon.in/")
    time.sleep(5)
    page.reload()
    time.sleep(5)


def test_refresh2(page: Page) -> None:
    page.goto("https://www.flipkart.com/")
    time.sleep(5)
    page.press("//a", "F5")
    time.sleep(5)
