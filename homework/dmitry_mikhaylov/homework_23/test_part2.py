from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

NAME_FIELD = (By.ID, "firstName")
LAST_NAME_FIELD = (By.ID, "lastName")
EMAIL_FIELD = (By.ID, "userEmail")
MALE_RADIO = (By.CSS_SELECTOR, "[value='Male']~label")
PHONE_FIELD = (By.ID, "userNumber")
BIRTHDATE_FIELD = (By.ID, "dateOfBirthInput")
SUBJECTS_FIELD = (By.ID, "subjectsInput")
SPORTS_CHKBOX = (By.CSS_SELECTOR, "#hobbies-checkbox-1~label")
READING_CHKBOX = (By.CSS_SELECTOR, "#hobbies-checkbox-2~label")
MUSIC_CHKBOX = (By.CSS_SELECTOR, "#hobbies-checkbox-3~label")
ADDRESS_FIELD = (By.ID, "currentAddress")
STATE_FIELD = (By.XPATH, "//div[text() = 'Select State']")
OPTION_ELEMENTS = (By.XPATH, "//div[contains(@id, 'option')]")
CITY_FIELD = (By.XPATH, "//div[text() = 'Select City']")
SUBMIT_BUTTON = (By.ID, "submit")
MODAL_TITLE = (By.XPATH, "//div[contains(@class, 'modal-title')]")
MODAL_HEADERS = (By.TAG_NAME, "th")
MODAIL_PAIRS = (By.TAG_NAME, "tr")
MODAL_ELEMENTS = (By.TAG_NAME, "td")


def output_info(data):
    if len(data) < 8:
        end = "\t" * 4
    elif 8 <= len(data) < 12:
        end = "\t" * 3
    else:
        end = "\t" * 2
    print(data, end=end)


def test_submit_form(driver):
    driver.get("https://demoqa.com/automation-practice-form")
    driver.execute_script("$('#fixedban').remove()")
    driver.execute_script("$('footer').remove()")

    driver.find_element(*NAME_FIELD).send_keys("Test")
    driver.find_element(*LAST_NAME_FIELD).send_keys("Test")
    driver.find_element(*EMAIL_FIELD).send_keys("test@test.com")
    driver.find_element(*MALE_RADIO).click()
    driver.find_element(*PHONE_FIELD).send_keys("1234567890")

    driver.find_element(*BIRTHDATE_FIELD).send_keys(Keys.CONTROL + "a")
    driver.find_element(*BIRTHDATE_FIELD).send_keys("15 Apr 1980")
    driver.find_element(*BIRTHDATE_FIELD).send_keys(Keys.ENTER)

    driver.find_element(*SUBJECTS_FIELD).send_keys("Computer")
    driver.find_elements(*OPTION_ELEMENTS)[0].click()
    driver.find_element(*SUBJECTS_FIELD).send_keys("English")
    driver.find_elements(*OPTION_ELEMENTS)[0].click()

    driver.find_element(*SPORTS_CHKBOX).click()
    driver.find_element(*READING_CHKBOX).click()
    driver.find_element(*MUSIC_CHKBOX).click()
    driver.find_element(*READING_CHKBOX).click()

    driver.find_element(*ADDRESS_FIELD).send_keys("ULY, Livanova pr-t, 123")

    driver.find_element(*STATE_FIELD).click()
    driver.find_elements(*OPTION_ELEMENTS)[0].click()
    driver.find_element(*CITY_FIELD).click()
    driver.find_elements(*OPTION_ELEMENTS)[0].click()

    driver.find_element(*SUBMIT_BUTTON).click()

    print(f"\n{driver.find_element(*MODAL_TITLE).text}")
    for element in driver.find_elements(*MODAL_HEADERS):
        output_info(element.text)
    print()
    for pair in driver.find_elements(*MODAIL_PAIRS):
        for element in pair.find_elements(*MODAL_ELEMENTS):
            output_info(element.text)
        print()
