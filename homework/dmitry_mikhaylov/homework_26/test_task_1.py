from playwright.sync_api import Page, expect

login = "tomsmith"
paswd = "SuperSecretPassword!"


def test_get_by_role(page: Page):
    page.goto("https://the-internet.herokuapp.com")
    page.get_by_role("link", name="Form Authentication").click()
    page.get_by_role("textbox", name="Username").fill(login)
    page.get_by_role("textbox", name="Password").fill(paswd)
    page.get_by_role("button", name="Login").click()
