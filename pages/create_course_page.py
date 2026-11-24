from playwright.sync_api import Page, expect

from pages.base_page import BasePage

from components.navigation.navbar_component import NavbarComponent
from components.views.empty_view_component import EmptyViewComponent
from components.views.image_upload_widget_component import ImageUploadWidgetComponent
from components.courses.create_course_form_component import CreateCourseFormComponent
from components.courses.create_course_toolbar_view_component import CreateCourseToolbarViewComponent
from components.courses.create_course_exercises_toolbar_view_component import CreateCourseExercisesToolbarViewComponent


class CreateCoursePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.preview_empty_view = EmptyViewComponent(page, 'create-course-preview')
        self.image_upload_widget = ImageUploadWidgetComponent(page, 'create-course-image-upload')
        self.exercises_empty_view = EmptyViewComponent(page,'create-course-exercises')
        self.create_course_form = CreateCourseFormComponent(page)
        self.create_course_toolbar = CreateCourseToolbarViewComponent(page)
        self.create_course_exercises_toolbar = CreateCourseExercisesToolbarViewComponent(page)

    def check_visible_create_course_title(self):
        expect(self.create_course_exercises_toolbar.title).to_be_visible()
        expect(self.create_course_exercises_toolbar.title).to_have_text('Create course')

    def click_create_course_button(self):
        self.create_course_exercises_toolbar.create_course_button.click()

    def check_visible_create_course_button(self):
        expect(self.create_course_exercises_toolbar.create_course_button).to_be_visible()

    def check_disabled_create_course_button(self):
        expect(self.create_course_exercises_toolbar.create_course_button).to_be_disabled()

    def check_visible_image_preview_empty_view(self):
        self.preview_empty_view.check_visible(
            title='No image selected',
            description='Preview of selected image will be displayed here'
        )

    def check_visible_image_upload_view(self, is_image_uploaded: bool = False):
        expect(self.image_upload_widget.image_upload_info_icon).to_be_visible()

        expect(self.image_upload_widget.image_upload_info_title).to_be_visible()
        expect(self.image_upload_widget.image_upload_info_title).to_have_text(
            'Tap on "Upload image" button to select file'
        )

        expect(self.image_upload_widget.image_upload_info_description).to_be_visible()
        expect(self.image_upload_widget.image_upload_info_description).to_have_text('Recommended file size 540X300')

        expect(self.image_upload_widget.image_upload_info_description).to_be_visible()

        if is_image_uploaded:
            expect(self.image_upload_widget.remove_button).to_be_visible()

    def click_remove_image_button(self):
        self.image_upload_widget.remove_button.click()

    def check_visible_preview_image(self):
        expect(self.image_upload_widget.preview_image).to_be_visible()

    def upload_preview_image(self, file: str):
        self.image_upload_widget.upload_input.set_input_files(file)

    def check_visible_create_course_form(
            self,
            title: str,
            estimated_time: str,
            description: str,
            max_score: str,
            min_score: str
    ):
        expect(self.create_course_form.title_input).to_be_visible()
        expect(self.create_course_form.title_input).to_have_value(title)

        expect(self.create_course_form.estimated_time_input).to_be_visible()
        expect(self.create_course_form.estimated_time_input).to_have_value(estimated_time)

        expect(self.create_course_form.description_textarea).to_be_visible()
        expect(self.create_course_form.description_textarea).to_have_value(description)

        expect(self.create_course_form.max_score_input).to_be_visible()
        expect(self.create_course_form.max_score_input).to_have_value(max_score)

        expect(self.create_course_form.min_score_input).to_be_visible()
        expect(self.create_course_form.min_score_input).to_have_value(min_score)

    def fill_create_course_form(
            self,
            title: str,
            estimated_time: str,
            description: str,
            max_score: str,
            min_score: str
    ):
        self.create_course_form.title_input.fill(title)
        expect(self.create_course_form.title_input).to_have_value(title)

        self.create_course_form.estimated_time_input.fill(estimated_time)
        expect(self.create_course_form.estimated_time_input).to_have_value(estimated_time)

        self.create_course_form.description_textarea.fill(description)
        expect(self.create_course_form.description_textarea).to_have_value(description)

        self.create_course_form.max_score_input.fill(max_score)
        expect(self.create_course_form.max_score_input).to_have_value(max_score)

        self.create_course_form.min_score_input.fill(min_score)
        expect(self.create_course_form.min_score_input).to_have_value(min_score)

    def check_visible_exercises_title(self):
        expect(self.create_course_toolbar.title).to_be_visible()
        expect(self.create_course_toolbar.title).to_have_text('Exercises')

    def check_visible_create_exercise_button(self):
        expect(self.create_course_toolbar.create_exercise_button).to_be_visible()

    def click_create_exercise_button(self):
        self.create_course_toolbar.create_exercise_button.click()

    def check_visible_exercises_empty_view(self):
        self.exercises_empty_view.check_visible(
            title='There is no exercises',
            description='Click on "Create exercise" button to create new exercise'
        )

    def click_delete_exercise_button(self, index: int):
        delete_exercise_button = self.page.get_by_test_id(
            f"create-course-exercise-{index}-box-toolbar-delete-exercise-button"
        )
        delete_exercise_button.click()

    def check_visible_create_exercise_form(self, index: int, title: str, description: str):
        exercise_subtitle = self.page.get_by_test_id(
            f"create-course-exercise-{index}-box-toolbar-subtitle-text"
        )
        exercise_title_input = self.page.get_by_test_id(
            f"create-course-exercise-form-title-{index}-input"
        )
        exercise_description_input = self.page.get_by_test_id(
            f"create-course-exercise-form-description-{index}-input"
        )

        expect(exercise_subtitle).to_be_visible()
        expect(exercise_subtitle).to_have_text(f"#{index + 1} Exercise")

        expect(exercise_title_input).to_be_visible()
        expect(exercise_title_input).to_have_value(title)

        expect(exercise_description_input).to_be_visible()
        expect(exercise_description_input).to_have_value(description)

    def fill_create_exercise_form(self, index: int, title: str, description: str):
        exercise_title_input = self.page.get_by_test_id(
            f"create-course-exercise-form-title-{index}-input"
        )
        exercise_description_input = self.page.get_by_test_id(
            f"create-course-exercise-form-description-{index}-input"
        )

        exercise_title_input.fill(title)
        expect(exercise_title_input).to_have_value(title)

        exercise_description_input.fill(description)
        expect(exercise_description_input).to_have_value(description)
