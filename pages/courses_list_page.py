from playwright.sync_api import Page, expect

from pages.base_page import BasePage

from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from components.views.empty_view_component import EmptyViewComponent
from components.courses.course_view_component import CourseViewComponent
from components.courses.courses_list_toolbar_view_component import CoursesListToolbarViewComponent


class CoursesListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)
        self.empty_view = EmptyViewComponent(page, 'courses-list')
        self.course_view = CourseViewComponent(page)
        self.courses_list_toolbar = CoursesListToolbarViewComponent(page)


    def check_visible_courses_title(self):
        expect(self.courses_list_toolbar.title).to_be_visible()
        expect(self.courses_list_toolbar.title).to_have_text('Courses')

    def check_visible_empty_view(self):
        self.empty_view.check_visible(
            title='There is no results',
            description='Results from the load test pipeline will be displayed here'
        )

    def check_visible_create_course_button(self):
        expect(self.courses_list_toolbar.create_course_button).to_be_visible()

    def click_create_course_button(self):
        self.courses_list_toolbar.create_course_button.click()