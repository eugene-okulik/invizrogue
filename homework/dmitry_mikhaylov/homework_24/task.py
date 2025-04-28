from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


def test_product_should_be_in_cart(driver):
    driver.get("https://www.demoblaze.com/index.html")
    wait = WebDriverWait(driver, 5)

    product_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'idp_=1') and text()]")))
    product_name = product_link.text
    ActionChains(driver).key_down(Keys.CONTROL).click(product_link).key_up(Keys.CONTROL).perform()

    driver.switch_to.window(driver.window_handles[1])
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[onclick^='addToCart']"))).click()

    alert = wait.until(EC.alert_is_present())
    alert.accept()

    driver.close()
    driver.switch_to.window(driver.window_handles[0])

    wait.until(EC.element_to_be_clickable((By.ID, "cartur"))).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, f"//td[text()='{product_name}']")))


def test_product_should_be_in_compare_section(driver):
    driver.get("https://magento.softwaretestingboard.com/gear/bags.html")
    wait = WebDriverWait(driver, 10)

    products = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-item-info")))
    product_img = products[3].find_element(By.CSS_SELECTOR, ".product-image-photo")
    product_compare_link = products[3].find_element(By.CSS_SELECTOR, "[title='Add to Compare']")
    product_name = product_img.get_attribute("alt")

    ActionChains(driver).move_to_element(product_img).click(product_compare_link).perform()
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//a[@title='Compare Products']"))
    )
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, f"//div[@data-role='compare-products-sidebar']//a[text()='{product_name}']"))
    )
