import re
import json

from playwright.sync_api import Page, Request, Response, Route


def test_should_change_product_name(page: Page):
    change_to_text = "яблокофон 16 про"

    def handle_route(route: Route):
        response = route.fetch()
        body = response.json()
        body["body"]["digitalMat"][0]["productName"] = change_to_text
        body = json.dumps(body)
        route.fulfill(
            response=response,
            body=body
        )

    page.route(re.compile(r"digital-mat"), handle_route)
    page.goto("https://www.apple.com/shop/buy-iphone")
    page.get_by_role("button", name="Take a closer look - iPhone 16 Pro & iPhone 16 Pro Max").click()

    assert (
            page.locator("button[class='rf-digitalmat-tabnav-button button button-neutral current']")
            .inner_text() == change_to_text
    )
