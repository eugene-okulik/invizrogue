import allure


@allure.feature("Проверка отображения количества карточек, в зависимости от выбранного значения в ограничителе")
def test_should_amount_cards_less_or_equal_amount_cards_selector_value(eco_friendly_page):
    eco_friendly_page.open()
    eco_friendly_page.select_cards_per_page("36")
    eco_friendly_page.check_amount_cards_less_or_equal_selected()
    eco_friendly_page.select_cards_per_page("24")
    eco_friendly_page.check_amount_cards_less_or_equal_selected()
    eco_friendly_page.select_cards_per_page("12")
    eco_friendly_page.check_amount_cards_less_or_equal_selected()


@allure.feature("Проверка добавления товара в избранное")
def test_should_product_in_wish_list(authorize_new_user, eco_friendly_page, wishlist_page):
    product_name = "Bella Tank"
    eco_friendly_page.open()
    eco_friendly_page.add_product_to_wishlist(product_name)
    wishlist_page.is_opened()
    wishlist_page.check_product_name_in_success_message(product_name)


@allure.feature("Проверка сортировки товаров по цене")
def test_should_sorting_by_price(eco_friendly_page):
    eco_friendly_page.open()
    eco_friendly_page.select_sorting_by_price()
    eco_friendly_page.check_products_sorted_by_price()
