import re
import allure
from test_UI_dmikhaylov.pages.base_page import BasePage
from playwright.sync_api import expect

list_of_products = ".item.product.product-item"
limiter_per_page_selector = ".products-grid~.toolbar.toolbar-products #limiter"
sorter_selector = "div.toolbar.toolbar-products:has(~.products-grid) #sorter"
product_in_wishlist = "#wishlist-sidebar .product-item"
item_price = ".item.product.product-item .price"


class EcoFriendlyPage(BasePage):
    page_url = "/collections/eco-friendly.html"

    @allure.step("Выбор сортировки по цене")
    def select_sorting_by_price(self):
        self.find(sorter_selector).select_option(label="Price")
        expect(self.page).to_have_url(re.compile(r"product_list_order=price$"), timeout=5000)

    @allure.step("Проверка, что товары отсортированы по цене")
    def check_products_sorted_by_price(self):
        item_prices = self.find_all(item_price)
        prices = [price.inner_text() for price in item_prices]
        sorted_prices = sorted(prices, key=lambda x: float(x.replace("$", "")))
        assert prices == sorted_prices

    @allure.step("Выбор количества карточек на странице")
    def select_cards_per_page(self, amount):
        self.find(limiter_per_page_selector).select_option(label=amount)

    @allure.step("Проверка, что отображаются карточки товаров в соответствии с выбранным количеством")
    def check_amount_cards_less_or_equal_selected(self):
        selected_amount = self.find(limiter_per_page_selector).input_value()
        products_on_page = self.find_all(list_of_products)
        assert len(products_on_page) <= int(selected_amount)

    @allure.step("Добавление товара в избранное")
    def add_product_to_wishlist(self, data):
        product_card = self.find(f"[alt='{data}']")
        add_to_wishlist_button = self.find(f"a:has([alt='{data}'])~div [title='Add to Wish List']")
        product_card.wait_for()
        product_card.hover()
        add_to_wishlist_button.click()
