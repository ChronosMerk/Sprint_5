from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locator as LC
import random


class TestCreateAd:
    def test_unauthenticated_user_create_ad_prompt(self, driver):
        driver.get('https://qa-desk.stand.praktikum-services.ru/')

        driver.find_element(*LC.HEADER_CREATE_AD).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LC.MODAL_WINDOW_AD_CREATE_NOT_AUTHORIZED_USER))

        modal_windows = driver.find_element(*LC.MODAL_WINDOW_AD_CREATE_NOT_AUTHORIZED_USER).text
        assert modal_windows  == 'Чтобы разместить объявление, авторизуйтесь'

    def test_authenticated_user_can_create_listing_and_see_it_in_profile(self, driver, authorized_user):
        driver.get('https://qa-desk.stand.praktikum-services.ru/')

        driver.find_element(*LC.HEADER_LOGIN_AND_REGISTRATION).click()
        driver.find_element(*LC.INPUT_EMAIL).send_keys(authorized_user["email"])
        driver.find_element(*LC.INPUT_PASSWORD).send_keys(authorized_user["password"])
        driver.find_element(*LC.BUTTON_LOGIN).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LC.COLUM_PROFILE_TEXT_NAME))
        driver.find_element(*LC.HEADER_CREATE_AD).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LC.CREATE_INPUT_NAME))
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LC.CREATE_INPUT_PRICE))
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LC.CREATE_TEXTAREA_DESCRIPTION))
        driver.find_element(*LC.CREATE_INPUT_NAME).send_keys(f'Kapibara {random.randint(1, 100)}')
        input_name = driver.find_element(*LC.CREATE_INPUT_NAME).get_attribute('value')
        driver.find_element(*LC.CREATE_INPUT_PRICE).send_keys(random.randint(1, 100))
        input_price = str(driver.find_element(*LC.CREATE_INPUT_PRICE).get_attribute('value'))
        driver.find_element(*LC.CREATE_TEXTAREA_DESCRIPTION).send_keys("Limon")

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(LC.CREATE_DROPDOWN_CITY_ARROW))
        driver.find_element(*LC.CREATE_DROPDOWN_CITY_ARROW).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_all_elements_located(LC.CREATE_DROPDOWN_CITY_BUTTONS))
        cities = driver.find_elements(*LC.CREATE_DROPDOWN_CITY_BUTTONS)
        city = random.choice(cities)
        city_name = city.text
        city.click()

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(LC.CREATE_DROPDOWN_CATEGORY_ARROW))
        driver.find_element(*LC.CREATE_DROPDOWN_CATEGORY_ARROW).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_all_elements_located(LC.CREATE_DROPDOWN_CATEGORY_BUTTONS))
        categories = driver.find_elements(*LC.CREATE_DROPDOWN_CATEGORY_BUTTONS)
        random.choice(categories).click()

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(LC.CREATE_FIELDSET_CONDITIONS_ACTIVE))
        driver.find_element(*LC.CREATE_FIELDSET_CONDITIONS_ACTIVE).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_all_elements_located(LC.CREATE_FIELDSET_CONDITIONS_REGULAR))
        conditions = driver.find_elements(*LC.CREATE_FIELDSET_CONDITIONS_REGULAR)
        random.choice(conditions).click()

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(LC.CREATE_BUTTON_PUBLISH))
        driver.find_element(*LC.CREATE_BUTTON_PUBLISH).click()

        created_entity = input_name, input_price, city_name

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LC.HOMEPAGE))
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(LC.HEADER_USER_AVATAR))
        driver.find_element(*LC.HEADER_USER_AVATAR).click()

        # Прокручиваем на последнюю страницу
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(LC.PROFILE_CARD_BUTTON_NEXT))
        not_last_page = len(driver.find_elements(*LC.PROFILE_CARD_BUTTON_NEXT_ACTIVE)) > 0
        while not_last_page:
            WebDriverWait(driver, 5).until(
                expected_conditions.element_to_be_clickable(LC.PROFILE_CARD_BUTTON_NEXT_ACTIVE))
            driver.find_element(*LC.PROFILE_CARD_BUTTON_NEXT_ACTIVE).click()

            # Явное ожидание хотя бы одной карточки на странице
            WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(LC.PROFILE_CARD_NAME))

            not_last_page = len(driver.find_elements(*LC.PROFILE_CARD_BUTTON_NEXT_ACTIVE)) > 0

        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(LC.PROFILE_CARD_DESCRIPTION_LAST))
        WebDriverWait(driver, 5).until(expected_conditions.text_to_be_present_in_element(LC.PROFILE_CARD_NAME, input_name))

        entity_name = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LC.PROFILE_CARD_NAME)).text
        entity_city = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LC.PROFILE_CARD_CITY)).text
        entity_price = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LC.PROFILE_CARD_PRICE)).text.replace(' ', '').replace('₽', '')

        assert created_entity == (entity_name, entity_price, entity_city)
