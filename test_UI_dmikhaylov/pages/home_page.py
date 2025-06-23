import allure
from test_UI_dmikhaylov.pages.base_page import BasePage

hot_sellers_title = "//h2[text()='Hot Sellers']"


class HomePage(BasePage):
    page_url = "/"

    @allure.step("Проверка наличия блока Hot Sellers на странице")
    def check_hot_sellers_block_exist(self):
        self.find(hot_sellers_title).is_visible()
