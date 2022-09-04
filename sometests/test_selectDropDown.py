import re

from playwright.sync_api import Page, expect
from playwright.sync_api import expect


def test_example(page: Page) -> None:
    # Go to https://selenium08.blogspot.com/2019/11/dropdown.html
    page.goto("https://selenium08.blogspot.com/2019/11/dropdown.html")

    # Select AF
    page.locator("select[name='country']").select_option(index=2)
    page.wait_for_timeout(3000)
    page.locator("select[name='country']").select_option(label="Barbados")
    # page.locator("//select[@name='country']").select_option(label="Barbados")
    # page.locator("//select[@name='Month']").select_option(['Jan', 'Feb', 'May'])
    # page.locator("//select[@name='Month']").select_text()
    page.wait_for_timeout(5000)
    # locator = page.locator("select[name='country']")
    # expect(locator).to_have_value(re.compile(r"Barbados"))
    # locator = page.locator("select[id='dropdown'] > option[selected='selected']")
    # print(locator.count())
    # print(locator.inner_text())


def test_example2(page: Page) -> None:
    # Go to https://selenium08.blogspot.com/2019/11/dropdown.html
    page.goto("https://the-internet.herokuapp.com/dropdown")

    # Select AF
    page.locator("select[id='dropdown']").select_option(label='Option 1')
    page.wait_for_timeout(3000)

    selected_loc = page.locator("select[id='dropdown'] > option[selected='selected']")
    print(selected_loc.count())
    print(selected_loc.inner_text())


def test_multiElements(page: Page) -> None:
    page.goto("https://selenium08.blogspot.com/2019/11/dropdown.html")
    page.wait_for_timeout(3000)
    country = page.locator("select[name='country']")
    country_dropdown = page.locator("select[name='country'] option")
    print(country_dropdown.count())
    # print(country_dropdown.all_inner_texts())
    country.click()
    i=0
    print(country_dropdown.first.text_content())
    print(country_dropdown.last.text_content())
    country_dropdown.last.click()
    # while i<country_dropdown.count():
    #     print(country_dropdown.nth(i).text_content())
    #     i = i+1;


