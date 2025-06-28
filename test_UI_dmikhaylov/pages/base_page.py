import allure
from playwright.sync_api import Page, expect, Locator


class BasePage:
    base_url = "https://magento.softwaretestingboard.com"
    page_url = None

    def __init__(self, page: Page):
        self.page = page

    @allure.step("Открытие страницы")
    def open(self):
        if self.page_url:
            self.page.goto(f"{self.base_url}{self.page_url}")
        else:
            raise NotImplementedError("Page can not be opened for this page class")

    @allure.step("Проверка открытия страницы")
    def is_opened(self):
        expect(self.page).to_have_url(f"{self.base_url}{self.page_url}")

    def find(self, locator) -> Locator:
        return self.page.locator(locator)

    def find_all(self, locator) -> list[Locator]:
        return self.page.locator(locator).all()
