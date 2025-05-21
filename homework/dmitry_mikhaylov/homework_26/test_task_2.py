from playwright.sync_api import Page, expect
from faker import Faker

fake = Faker()


def test_filling_form_by_playwright(page: Page):
    page.goto("https://demoqa.com/automation-practice-form", wait_until='domcontentloaded')

    page.locator("#fixedban").evaluate("el => el.remove()")
    page.locator("footer").evaluate("el => el.remove()")

    page.get_by_role("textbox", name="First Name").fill(fake.first_name())
    page.get_by_role("textbox", name="Last Name").fill(fake.last_name())

    page.locator("#userEmail").fill(fake.email())

    page.get_by_text("Male", exact=True).click()

    page.get_by_placeholder("Mobile Number").fill("1234567890")
    page.get_by_placeholder("Mobile Number").blur()

    page.locator("#dateOfBirthInput").fill("06 Jun 1980")
    page.locator("#dateOfBirthInput").blur()

    page.locator("#subjectsInput").fill("Computer")
    page.get_by_text("Computer Science", exact=True).click()

    page.get_by_text("Sports").click()
    page.get_by_text("Reading").click()
    page.get_by_text("Music").click()

    page.get_by_placeholder("Current Address").fill(fake.address())
    page.get_by_text("Select State").click()
    page.get_by_text("NCR", exact=True).click()

    page.get_by_text("Select City").click()
    page.get_by_text("Delhi", exact=True).click()
    page.get_by_text("Submit").click()
