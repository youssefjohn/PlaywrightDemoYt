import time

from playwright.sync_api import Page


def test_element_hidden_appear_after_some_time(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/dynamic_loading/1")
    page.locator("button", has_text='Start').click()

    text_final = page.locator("#finish h4")
    print(text_final.inner_text())

def test_element_hidden_appear_after_some_time2(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/dynamic_loading/2")
    page.locator("button", has_text='Start').click()

    text_final = page.locator("#finish h4")
    text_final.wait_for(state='hidden')
    print(text_final.inner_text())

def test_ajax_call(page: Page) -> None:
    page.goto("http://uitestingplayground.com/ajax")
    page.locator('text=Button Triggering AJAX Request').click()

    result = page.locator("p.bg-success")
    print(result.inner_text())

def test_auto_wait_sauce_demo(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("wrong_sauce")
    page.locator("#login-button").click()
    error_text = page.locator("//div[@class='error-message-container error']/h3")
    # error_text.wait_for()
    expected_err_text = "Username and password do not match any user in this service"
    assert expected_err_text in error_text.inner_text(), "Correct error message is not dispalyed"



