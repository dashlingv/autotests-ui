from typing import Pattern

from playwright.sync_api import Page, expect


class BaseComponent:
    def __init__(self, page: Page):
        self.page = page

    def refresh_page(self, expected_url: Pattern[str]):
        self.page.reload()
        expect(self.page).to_have_url(expected_url)
