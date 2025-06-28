import pytest
from playwright.sync_api import BrowserContext
from faker import Faker
from test_UI_dmikhaylov.pages.home_page import HomePage
from test_UI_dmikhaylov.pages.sale_page import SalePage
from test_UI_dmikhaylov.pages.wishlist_page import WishlistPage
from test_UI_dmikhaylov.pages.eco_friendly_page import EcoFriendlyPage
from test_UI_dmikhaylov.pages.customer_account_page import CustomerAccountPage
from test_UI_dmikhaylov.pages.promotions_women_sale_page import PromotionsWomenSalePage
from test_UI_dmikhaylov.pages.customer_account_create_page import CustomerAccountCreatePage


@pytest.fixture()
def page(context: BrowserContext):
    page = context.new_page()
    page.set_viewport_size({"width": 1920, "height": 1080})
    return page


@pytest.fixture()
def home_page(page):
    return HomePage(page)


@pytest.fixture()
def sale_page(page):
    return SalePage(page)


@pytest.fixture()
def women_sale_page(page):
    return PromotionsWomenSalePage(page)


@pytest.fixture()
def account_create_page(page):
    return CustomerAccountCreatePage(page)


@pytest.fixture()
def wishlist_page(page):
    return WishlistPage(page)


@pytest.fixture()
def account_page(page):
    return CustomerAccountPage(page)


@pytest.fixture()
def eco_friendly_page(page):
    return EcoFriendlyPage(page)


@pytest.fixture()
def authorize_new_user(account_create_page, account_page, person):
    account_name = person["firstname"]
    account_lastname = person["lastname"]
    account_email = person["email"]
    account_create_page.open()
    account_create_page.fill_form(account_name, account_lastname, account_email)
    account_create_page.click_create_button()
    account_page.is_opened()


@pytest.fixture()
def person():
    faker = Faker()
    return {
        'firstname': faker.first_name(),
        'lastname': faker.last_name(),
        'email': faker.email(),
        'password': faker.password()
    }
