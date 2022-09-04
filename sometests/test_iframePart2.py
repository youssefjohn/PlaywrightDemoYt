import time

from playwright.sync_api import Page


def test_switch_frame_by_name(page: Page) -> None:
    page.goto("https://www.rediff.com/")
    # nse_index = page.frame("moneyiframe").locator("span#nseindex").text_content()
    # nse_index = page.main_frame.child_frames[0].locator("span#nseindex").text_content()
    nse_index = get_child_frame_by_index(page.main_frame, 0).locator("span#nseindex").text_content()
    print(nse_index)
    page.wait_for_timeout(1000)
    for child_frame in page.main_frame.child_frames:
        print(child_frame.name)


def test_switch_frame_by_index(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/nested_frames")
    for child_frame in page.main_frame.child_frames:
        print(child_frame.name)

    # top_frame = get_child_frame_by_index(page.main_frame, 0)
    # left_frame = get_child_frame_by_index(top_frame, 0)
    # print(left_frame.locator("body").inner_text())

    main_frame = page.main_frame
    print(type(main_frame))
    top_frame = main_frame.child_frames[0]
    bottom_frame = main_frame.child_frames[1]

    left_frame = top_frame.child_frames[0]
    middle_frame = top_frame.child_frames[1]
    right_frame = top_frame.child_frames[2]

    left_frame_text = left_frame.locator("body").inner_text()
    print(left_frame_text)
    middle_frame_text = middle_frame.locator("body").inner_text()
    print(middle_frame_text)
    right_frame_text = right_frame.locator("body").inner_text()
    print(right_frame_text)


def get_child_frame_by_index(main_frame, index):
    return main_frame.child_frames[index]
