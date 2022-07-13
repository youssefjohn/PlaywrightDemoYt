import time

import pytest


@pytest.fixture(scope='session')
def setup_context1(playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    # page.set_viewport_size({"width": 1536, "height": 800})
    page.goto("https://the-internet.herokuapp.com/login", wait_until="networkidle")
    page.locator("#username").fill("tomsmith", timeout=5000)
    page.locator("#password").fill("SuperSecretPassword!")
    page.locator("//button[@type='submit']").click()
    # Save storage state into the file.
    # context.storage_state(path="state.json")
    time.sleep(2)
    yield context
    time.sleep(5)


@pytest.fixture(scope='function')
def set_up_teardown(setup_context1, browser) -> None:
    # context = browser.new_context(storage_state='state.json')
    context = browser.new_context()
    # context = setup_context1
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/secure")
    time.sleep(5)
    yield page
    time.sleep(5)
    context.close()

