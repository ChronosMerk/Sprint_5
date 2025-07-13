from selenium.webdriver.common.by import By

class Locator:
    HEADER_LOGIN_AND_REGISTRATION = By.XPATH, ".//div[contains(@class,'header_')]/button[text()='Вход и регистрация']"
    POP_BUTTON_NO_ACCOUNT = By.XPATH, ".//div[contains(@class,'popUp_button')]//button[text()='Нет аккаунта']"
    POP_INPUTS = By.XPATH, ".//div[@class='popUp_inputColumn__RgD8n']//input"
    INPUT_EMAIL = By.NAME, "email"
    INPUT_PASSWORD = By.NAME, "password"
    INPUT_SUBMIT_PASSWORD = By.NAME, "submitPassword"
    POP_BUTTON_CREATE_ACCOUNT = By.XPATH,".//div[contains(@class , 'popUp_')]/button[text() = 'Создать аккаунт']"
    HEADER_AVATAR = By.CLASS_NAME, "svgSmall"
    COLUM_PROFILE_TEXT_NAME = By.XPATH, ".//h3[@class = 'profileText name']"
    ERROR_MESSAGE_REGISTRATION_NOT_VALUE_EMAIL = By.XPATH, ".//span[text() = 'Ошибка']"
    FRAME_INPUT_ERROR = By.XPATH, ".//div[@class='popUp_inputColumn__RgD8n']//div[@class='input_inputError__fLUP9']"