import time

from playwright.sync_api import Page


def test_iframe(page: Page) -> None:
    page.goto("https://jqueryui.com/autocomplete/")
    input_field = page.frame_locator("iframe.demo-frame").locator("input.ui-autocomplete-input")
    input_field.fill("E")
    page.wait_for_timeout(3000)


def test_iframe_example2(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/iframe")
    element = page.frame("mce_0_ifr").locator("body#tinymce")
    element.click()
    # page.keyboard.press("Control+A")
    element.press("Control+A")
    element.type("AutomationNeemo")
    page.wait_for_timeout(3000)
