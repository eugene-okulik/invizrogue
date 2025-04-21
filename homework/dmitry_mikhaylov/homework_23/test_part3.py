from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_choosing_language(driver):
    driver.get("https://www.qa-practice.com/elements/select/single_select")
    language = "Ruby"
    button = driver.find_element(By.NAME, "submit")
    select = driver.find_element(By.NAME, "choose_language")
    elements = Select(select)
    elements.select_by_visible_text(language)
    button.click()
    assert driver.find_element(By.ID, "result-text").get_attribute("innerText") == language


def test_starting(driver):
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    driver.find_element(By.TAG_NAME, "button").click()
    wait = WebDriverWait(driver, 30)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//h4[text()='Hello World!']")))
    assert driver.find_element(By.XPATH, "//h4[text()='Hello World!']").is_displayed()
