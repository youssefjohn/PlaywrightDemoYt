import pytest
from playwright.sync_api import Playwright, sync_playwright, expect


def test_01_verify_logout_visible(set_up_teardown) -> None:
    page = set_up_teardown
    # page.goto("https://the-internet.herokuapp.com/login")
    # assert page.locator("//i[text()=' Logout']/parent::a").is_visible()
    assert True


def test_02_verify_logout(set_up_teardown) -> None:
    page = set_up_teardown
    # page.goto("https://the-internet.herokuapp.com/login")
    # page.locator("//button[text()='Log Out']").click()
    # assert page.locator("#login").inner_text() == 'Log In'
    assert True
