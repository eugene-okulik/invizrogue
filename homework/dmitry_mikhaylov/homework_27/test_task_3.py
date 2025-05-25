from playwright.sync_api import Page, expect
import re


def test_should_click_button_after_change_color(page: Page):
    page.goto("https://demoqa.com/dynamic-properties", wait_until='domcontentloaded')
    button = page.get_by_role("button", name="Color Change")
    expect(button).to_have_css("color", re.compile(r"rgb\(220,\s*53,\s*69\)|red"), timeout=10000)
    button.click()
