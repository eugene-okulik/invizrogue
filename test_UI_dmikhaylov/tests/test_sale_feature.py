import allure


@allure.feature("Проверка перехода на страницу с акционными товарами для женщин")
def test_should_open_women_sale_page(sale_page, women_sale_page):
    sale_page.open()
    sale_page.click_women_deals()
    women_sale_page.is_opened()
    women_sale_page.check_page_name()


@allure.feature("Проверка отображения сообщения о пустой корзине")
def test_should_get_message_on_click_empty_cart(sale_page):
    sale_page.open()
    sale_page.click_cart_button()
    sale_page.check_empty_cart_message_exist()


@allure.feature("Проверка перехода на главную страницу по клику в навигационном меню")
def test_should_open_home_page_on_click_link_in_nav_menu(sale_page, home_page):
    sale_page.open()
    sale_page.click_home_page_link()
    home_page.is_opened()
    home_page.check_hot_sellers_block_exist()
