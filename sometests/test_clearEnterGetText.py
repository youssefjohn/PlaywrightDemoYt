from playwright.sync_api import Page, expect
import time


def clear_text(page, locator):
    page.press(locator, 'Control+KeyA')
    page.press(locator, 'Backspace')


def test_example(page: Page) -> None:

    # Go to https://the-internet.herokuapp.com/login
    page.goto("https://the-internet.herokuapp.com/login")
    username = page.locator('#username')
    username.fill('tomsmith1')
    page.locator('#password').fill('SuperSecretPassword!')
    clear_text(page, '#username')

    time.sleep(3)


