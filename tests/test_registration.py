from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locator as LC
import pytest

class TestRegistration:
    def test_registration_valid_unique_credentials(self, driver, generate_random_password, generate_random_email):
        driver.get('https://qa-desk.stand.praktikum-services.ru/')

        driver.find_element(*LC.HEADER_LOGIN_AND_REGISTRATION).click()
        driver.find_element(*LC.POP_BUTTON_NO_ACCOUNT).click()

        login = generate_random_email
        password = generate_random_password

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LC.POP_INPUTS))
        driver.find_element(*LC.INPUT_EMAIL).send_keys(login)
        driver.find_element(*LC.INPUT_PASSWORD).send_keys(password)
        driver.find_element(*LC.INPUT_SUBMIT_PASSWORD).send_keys(password)
        driver.find_element(*LC.POP_BUTTON_CREATE_ACCOUNT).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LC.COLUM_PROFILE_TEXT_NAME))
        assert driver.find_element(*LC.HEADER_AVATAR)
        assert driver.find_element(*LC.COLUM_PROFILE_TEXT_NAME).text =='User.'

    @pytest.mark.parametrize('email',[
    "plainaddress",
    "missingatsign.com",
    "@no-local-part.com",
    "name@.com",
    "name@domain",
    "name@domain..com",
    "name@domain.c",
    "name@domain,com",
])
    def test_registration_with_invalid_email_shows_error_and_highlights_fields(self, driver, generate_random_password, email):
        driver.get('https://qa-desk.stand.praktikum-services.ru/')

        driver.find_element(*LC.HEADER_LOGIN_AND_REGISTRATION).click()
        driver.find_element(*LC.POP_BUTTON_NO_ACCOUNT).click()
        password = generate_random_password

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LC.POP_INPUTS))
        driver.find_element(*LC.INPUT_EMAIL).send_keys(email)
        driver.find_element(*LC.INPUT_PASSWORD).send_keys(password)
        driver.find_element(*LC.INPUT_SUBMIT_PASSWORD).send_keys(password)
        driver.find_element(*LC.POP_BUTTON_CREATE_ACCOUNT).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LC.ERROR_MESSAGE_REGISTRATION_NOT_VALUE_EMAIL))
        message_error = driver.find_element(*LC.ERROR_MESSAGE_REGISTRATION_NOT_VALUE_EMAIL).text
        frame_error = driver.find_elements(*LC.FRAME_INPUT_ERROR)
        assert len(frame_error) == 3 and message_error == 'Ошибка'

    def test_registration_with_existing_user_shows_error_and_highlights_fields(self, driver):
        driver.get('https://qa-desk.stand.praktikum-services.ru/')
        email = 'hbol@gmail.com'
        password = 'hbol'

        driver.find_element(*LC.HEADER_LOGIN_AND_REGISTRATION).click()
        driver.find_element(*LC.POP_BUTTON_NO_ACCOUNT).click()


        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LC.POP_INPUTS))
        driver.find_element(*LC.INPUT_EMAIL).send_keys(email)
        driver.find_element(*LC.INPUT_PASSWORD).send_keys(password)
        driver.find_element(*LC.INPUT_SUBMIT_PASSWORD).send_keys(password)
        driver.find_element(*LC.POP_BUTTON_CREATE_ACCOUNT).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LC.ERROR_MESSAGE_REGISTRATION_NOT_VALUE_EMAIL))
        message_error = driver.find_element(*LC.ERROR_MESSAGE_REGISTRATION_NOT_VALUE_EMAIL).text
        frame_error = driver.find_elements(*LC.FRAME_INPUT_ERROR)
        assert len(frame_error) == 3 and message_error == 'Ошибка'