from playwright.sync_api import expect
import pytest

from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage


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


@pytest.mark.courses
@pytest.mark.regression
def test_create_course(create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
    create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
    create_course_page.check_visible_create_course_title()
    create_course_page.check_disabled_create_course_button()
    create_course_page.check_visible_image_preview_empty_view()
    create_course_page.check_visible_image_upload_view()
    create_course_page.check_visible_create_course_form(
        title="",
        estimated_time="",
        description="",
        max_score="0",
        min_score="0"
    )
    create_course_page.check_visible_exercises_title()
    create_course_page.check_visible_create_exercise_button()
    create_course_page.check_visible_exercises_empty_view()

    create_course_page.upload_preview_image("./testdata/files/image.png")
    create_course_page.check_visible_image_upload_view()
    create_course_page.fill_create_course_form(
        title="Playwright",
        estimated_time="2 weeks",
        description="Playwright",
        max_score="100",
        min_score="10"
    )
    create_course_page.click_create_course_button()

    courses_list_page.check_visible_courses_title()
    courses_list_page.check_visible_create_course_button()
    courses_list_page.check_visible_course_card(
        index=0,
        title="Playwright",
        max_score="100",
        min_score="10",
        estimated_time="2 weeks"
    )
