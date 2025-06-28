import allure
from playwright.sync_api import expect

from test_UI_dmikhaylov.pages.base_page import BasePage

firstname_field = "#firstname"
firstname_error = "#firstname-error"
lastname_field = "#lastname"
lastname_error = "#lastname-error"
email_address_field = "#email_address"
email_address_error = "#email_address-error"
password_field = "#password"
password_error = "#password-error"
password_confirm_field = "#password-confirmation"
password_confirm_error = "#password-confirmation-error"
create_button = "button[title='Create an Account']"
wellcome_message = ".logged-in"
empty_error_text = "This is a required field."
not_match_error_text = "Please enter the same value again."


class CustomerAccountCreatePage(BasePage):
    page_url = "/customer/account/create/"

    @allure.step("Заполнение поля Name")
    def fill_firstname(self, data):
        self.find(firstname_field).is_disabled()
        self.find(firstname_field).fill(data)

    @allure.step("Заполнение поля Lastname")
    def fill_lastname(self, data):
        self.find(lastname_field).is_visible()
        self.find(lastname_field).fill(data)

    @allure.step("Заполнение поля Email")
    def fill_email(self, data):
        self.find(email_address_field).is_visible()
        self.find(email_address_field).fill(data)

    @allure.step("Заполнение поля Password")
    def fill_password(self, data):
        self.find(password_field).is_visible()
        self.find(password_field).fill(data)

    @allure.step("Заполнение поля Password Confirm")
    def fill_password_confirm(self, data):
        self.find(password_confirm_field).is_visible()
        self.find(password_confirm_field).fill(data)

    @allure.step("Проверка, что отображается сообщение об ошибке заполнения поля Name")
    def check_empty_firstname_error_exist(self):
        self.find(firstname_error).is_visible()
        expect(self.find(firstname_error)).to_have_text(empty_error_text)
        # assert self.find(firstname_error).inner_text() == empty_error_text

    @allure.step("Проверка, что отображается сообщение об ошибке заполнения поля Lastame")
    def check_empty_lastname_error_exist(self):
        self.find(lastname_error).is_visible()
        expect(self.find(lastname_error)).to_have_text(empty_error_text)
        # assert self.find(lastname_error).inner_text() == empty_error_text

    @allure.step("Проверка, что отображается сообщение об ошибке заполнения поля Email")
    def check_empty_email_error_exist(self):
        self.find(email_address_error).is_visible()
        expect(self.find(email_address_error)).to_have_text(empty_error_text)
        # assert self.find(email_address_error).inner_text() == empty_error_text

    @allure.step("Проверка, что отображается сообщение об ошибке заполнения поля Password")
    def check_empty_password_error_exist(self):
        self.find(password_error).is_visible()
        expect(self.find(password_error)).to_have_text(empty_error_text)
        # assert self.find(password_error).inner_text() == empty_error_text

    @allure.step("Проверка, что отображается сообщение об ошибке заполнения поля Password Confirm")
    def check_empty_password_confirm_error_exist(self):
        self.find(password_confirm_error).is_visible()
        expect(self.find(password_confirm_error)).to_have_text(empty_error_text)
        # assert self.find(password_confirm_error).inner_text() == empty_error_text

    @allure.step("Проверка, что отображается сообщение об ошибке несовпадения паролей")
    def check_not_match_password_confirm_error_exist(self):
        self.find(password_confirm_error).is_visible()
        expect(self.find(password_confirm_error)).to_have_text(not_match_error_text)

    @allure.step("Нажатие кнопки Create an Account")
    def click_create_button(self):
        self.find(create_button).is_visible()
        self.find(create_button).click()

    @allure.step("Заполнение формы создания аккаунта")
    def fill_form(self, firstname, lastname, email, password="Test@123456!"):
        self.fill_firstname(firstname)
        self.fill_lastname(lastname)
        self.fill_email(email)
        self.fill_password(password)
        self.fill_password_confirm(password)
