from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locator as LC

class TestLogin:
    def test_user_login_and_avatar_display(self, driver, authorized_user):
        driver.get('https://qa-desk.stand.praktikum-services.ru/')

        driver.find_element(*LC.HEADER_LOGIN_AND_REGISTRATION).click()
        driver.find_element(*LC.INPUT_EMAIL).send_keys(authorized_user['email'])
        driver.find_element(*LC.INPUT_PASSWORD).send_keys(authorized_user['password'])
        driver.find_element(*LC.BUTTON_LOGIN).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LC.COLUM_PROFILE_TEXT_NAME))
        assert driver.find_element(*LC.COLUM_PROFILE_TEXT_NAME).text == 'User.' and driver.find_element(*LC.HEADER_AVATAR)

