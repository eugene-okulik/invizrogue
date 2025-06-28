import allure


@allure.feature("Проверка отображения ошибок незаполненных обязательных полей при создании аккаунта")
def test_should_errors_exist_on_empty_fields(account_create_page):
    account_create_page.open()
    account_create_page.click_create_button()
    account_create_page.check_empty_firstname_error_exist()
    account_create_page.check_empty_lastname_error_exist()
    account_create_page.check_empty_email_error_exist()
    account_create_page.check_empty_password_error_exist()
    account_create_page.check_empty_password_confirm_error_exist()


@allure.feature("Проверка отображения ошибки несовпадения паролей при создании аккаунта")
def test_should_error_exist_on_not_matched_passwords(account_create_page):
    account_create_page.open()
    account_create_page.fill_password("Test!123456!")
    account_create_page.fill_password_confirm("Test@1234567!")
    account_create_page.click_create_button()
    account_create_page.check_not_match_password_confirm_error_exist()


@allure.feature("Проверка отображения информации о созданном аккаунте")
def test_should_displayed_account_info_on_successful_created_account(person, account_create_page, account_page):
    account_name = person["firstname"]
    account_lastname = person["lastname"]
    account_email = person["email"]
    account_create_page.open()
    account_create_page.fill_form(account_name, account_lastname, account_email)
    account_create_page.click_create_button()
    account_page.is_opened()
    account_page.check_success_message_displayed()
    account_page.check_welcome_message_displayed(account_name, account_lastname)
