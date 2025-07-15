import os


class URL:
    BASE = "https://qa-desk.stand.praktikum-services.ru/"


class User:
    EMAIL = os.getenv("QA_EMAIL", "test@example.com")
    PASSWORD = os.getenv("QA_PASSWORD", "password")
