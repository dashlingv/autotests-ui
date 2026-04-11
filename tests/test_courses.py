from playwright.sync_api import expect


def test_empty_courses_list(chromium_page_with_state):
    chromium_page_with_state.goto(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses"
    )
    main_header = chromium_page_with_state.get_by_test_id("courses-list-toolbar-title-text")
    expect(main_header).to_be_visible()
    expect(main_header).to_have_text("Courses")

    text_result = chromium_page_with_state.get_by_test_id("courses-list-empty-view-title-text")
    expect(text_result).to_be_visible()
    expect(text_result).to_have_text("There is no results")

    icon = chromium_page_with_state.get_by_test_id("courses-list-empty-view-icon")
    expect(icon).to_be_visible()

    text_information = chromium_page_with_state.get_by_test_id("courses-list-empty-view-description-text")
    expect(text_information).to_be_visible()
    expect(text_information).to_have_text(
        "Results from the load test pipeline will be displayed here"
    )
