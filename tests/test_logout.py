from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locator as LC
from data import User, URL

class TestLogout:
    def test_user_logout_hides_avatar_and_shows_login_button(self, driver):
        driver.get(URL.BASE)

        driver.find_element(*LC.HEADER_LOGIN_AND_REGISTRATION).click()
        driver.find_element(*LC.INPUT_EMAIL).send_keys(User.EMAIL)
        driver.find_element(*LC.INPUT_PASSWORD).send_keys(User.PASSWORD)
        driver.find_element(*LC.BUTTON_LOGIN).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LC.COLUM_PROFILE_TEXT_NAME))
        driver.find_element(*LC.COLUM_PROFILE_EXIT).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LC.HEADER_LOGIN_AND_REGISTRATION))
        user_avatar = driver.find_elements(*LC.HEADER_AVATAR)
        button_registration = driver.find_element(*LC.HEADER_LOGIN_AND_REGISTRATION).text

        assert button_registration == 'Вход и регистрация'
        assert len(user_avatar) == 0
