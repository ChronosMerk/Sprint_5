from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locator as LC
from data import URL,User

class TestLogin:
    def test_user_login_and_avatar_display(self, driver):
        driver.get(URL.BASE)

        driver.find_element(*LC.HEADER_LOGIN_AND_REGISTRATION).click()
        driver.find_element(*LC.INPUT_EMAIL).send_keys(User.EMAIL)
        driver.find_element(*LC.INPUT_PASSWORD).send_keys(User.PASSWORD)
        driver.find_element(*LC.BUTTON_LOGIN).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LC.COLUM_PROFILE_TEXT_NAME))
        assert driver.find_element(*LC.COLUM_PROFILE_TEXT_NAME).text == 'User.' and driver.find_element(*LC.HEADER_AVATAR)
