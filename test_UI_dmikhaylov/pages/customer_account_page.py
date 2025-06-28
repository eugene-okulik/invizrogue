import allure
from playwright.sync_api import expect

from test_UI_dmikhaylov.pages.base_page import BasePage

welcome_message = ".box-information .box-content p"
success_messages = "//div[contains(@data-ui-id, 'message-success')]//div"
success_account_creation_message = "Thank you for registering with Main Website Store."


class CustomerAccountPage(BasePage):
    page_url = "/customer/account/"

    @allure.step("Проверка, что отображается сообщение об успешном создании аккаунта")
    def check_success_message_displayed(self):
        expect(self.find(success_messages)).to_have_text(success_account_creation_message)

    @allure.step("Проверка, что отображается приветственное сообщение с фамилией и именем")
    def check_welcome_message_displayed(self, first_name, last_name):
        expect(self.find(welcome_message)).to_contain_text(f"{first_name} {last_name}")
