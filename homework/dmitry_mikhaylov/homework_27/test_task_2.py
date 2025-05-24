from playwright.sync_api import Page, BrowserContext


def test_should_open_new_tab(page: Page, context: BrowserContext):
    page.goto("https://www.qa-practice.com/elements/new_tab/button")
    link = page.get_by_role("link", name="Click")
    with context.expect_page() as new_page_event:
        link.click()

    new_page = new_page_event.value
    new_page.locator("#result-text", has_text="I am a new page in a new tab").is_visible()

    link.is_enabled()
    # page.get_by_role("link", name="Click").is_enabled()
