import random
import string
import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def generate_random_email():
        username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        domain = random.choice(['gmail.com', 'yahoo.com', 'test.com'])
        return f"{username}@{domain}"

@pytest.fixture
def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    return password

@pytest.fixture
def authorized_user():
    user = {
        "email": "hbol@gmail.com",
        "password": "hbol"
    }
    return user