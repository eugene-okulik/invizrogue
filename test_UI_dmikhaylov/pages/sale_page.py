import allure
from playwright.sync_api import expect

from test_UI_dmikhaylov.pages.base_page import BasePage

women_deals_link = "//span[text()='Women’s Deals']"
cart_button = ".action.showcart"
empty_cart_message = ".subtitle.empty"
empty_message_text = "You have no items in your shopping cart."
home_page_link = "a[title='Go to Home Page']"


class SalePage(BasePage):
    page_url = "/sale.html"

    @allure.step("Клик по ссылке 'Women’s Deals'")
    def click_women_deals(self):
        self.find(women_deals_link).click()

    @allure.step("Клик по кнопке 'Cart'")
    def click_cart_button(self):
        self.find(cart_button).click()

    @allure.step("Проверка отображения сообщения о пустой корзине")
    def check_empty_cart_message_exist(self):
        # empty_message = self.find(empty_cart_message)
        expect(self.find(empty_cart_message)).to_have_text(empty_message_text)
        # assert empty_message.inner_text() == empty_message_text

    @allure.step("Клик по ссылке 'Home'")
    def click_home_page_link(self):
        self.find(home_page_link).click()
