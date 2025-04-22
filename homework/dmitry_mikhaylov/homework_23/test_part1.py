from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_search_entered_text(driver):
    test_data = "HelloWorld"
    driver.get("https://www.qa-practice.com/elements/input/simple")
    wait = WebDriverWait(driver, 5)

    text_field = driver.find_element(By.NAME, "text_string")
    text_field.send_keys(test_data)
    text_field.submit()
    wait.until(EC.visibility_of_element_located((By.ID, "result-text")))
    assert driver.find_element(By.ID, "result-text").text == test_data
