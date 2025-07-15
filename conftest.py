import os
import pytest
from selenium import webdriver
from helpers import generate_random_email as _generate_random_email, generate_random_password as _generate_random_password

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    if os.getenv("HEADLESS", "1") == "1":
        options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(3)
    yield driver
    driver.quit()


@pytest.fixture
def generate_random_email():
    return _generate_random_email()


@pytest.fixture
def generate_random_password():
    return _generate_random_password()
