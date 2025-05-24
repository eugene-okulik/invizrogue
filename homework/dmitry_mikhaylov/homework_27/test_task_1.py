from playwright.sync_api import Page


def test_should_be_ok_in_you_selected_section(page: Page):
    page.goto("https://www.qa-practice.com/elements/alert/confirm")
    page.get_by_role("link", name="Click").click()
    page.on("dialog", lambda dialog: dialog.accept())
    page.locator("#result-text", has_text="Ok").is_visible()
