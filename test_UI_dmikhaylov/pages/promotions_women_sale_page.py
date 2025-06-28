import allure
from playwright.sync_api import expect

from test_UI_dmikhaylov.pages.base_page import BasePage

page_name = "h1"
page_name_text = "Women Sale"


class PromotionsWomenSalePage(BasePage):
    page_url = "/promotions/women-sale.html"

    @allure.step("Проверка названия страницы")
    def check_page_name(self):
        self.find(page_name)
        expect(self.find(page_name)).to_have_text(page_name_text)
        # assert self.find(page_name).inner_text() == page_name_text
