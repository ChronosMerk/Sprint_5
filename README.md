# 🧪 UI Автотесты для платформы QA Desk

Проект содержит автотесты, написанные с использованием **Selenium WebDriver** и **Pytest**. Тестируется регистрация, авторизация, выход из аккаунта и создание объявлений на платформе [qa-desk.stand.praktikum-services.ru](https://qa-desk.stand.praktikum-services.ru/).

---

## 📂 Содержание

- [Установка](#установка)
- [Структура проекта](#структура-проекта)
- [Описание файлов](#описание-файлов)
  - [conftest.py](#-conftestpy)
  - [locators.py](#-locatorspy)
  - [test_login.py](#-test_loginpy)
  - [test_logout.py](#-test_logoutpy)
  - [test_registration.py](#-test_registrationpy)
  - [test_create_an_ad.py](#-test_create_an_adpy)
- [Запуск тестов](#запуск-тестов)
- [Рекомендации](#рекомендации)

---

## 🔧 Установка

```bash
pip install -r requirements.txt
Убедитесь, что установлен ChromeDriver, совместимый с версией вашего браузера.

🗂️ Структура проекта
├── conftest.py              # Общие фикстуры
├── locators.py              # Page Object локаторы
├── test_login.py            # Тесты на авторизацию
├── test_logout.py           # Тесты на выход
├── test_registration.py     # Тесты на регистрацию
├── test_create_an_ad.py     # Тесты на создание объявления
🔧 conftest.py
Файл conftest.py содержит фикстуры Pytest:

driver — инициализация ChromeDriver.
generate_random_email — случайный email.
generate_random_password(length=12) — случайный пароль.

📍 locators.py
Содержит локаторы в формате Page Object Model.
Примеры:
Назначение	Локатор
Кнопка входа	HEADER_LOGIN_AND_REGISTRATION
Поле email	INPUT_EMAIL
Кнопка "Опубликовать"	CREATE_BUTTON_PUBLISH
Имя пользователя в профиле	COLUM_PROFILE_TEXT_NAME

✅ test_login.py
Проверяет успешную авторизацию:
Открытие сайта.
Ввод email и пароля.
Проверка отображения имени пользователя и аватара.

🔓 test_logout.py
Проверяет корректность выхода:
Выполняется логин.
Кликается кнопка "Выйти".
Проверяется отсутствие аватара и повторное появление кнопки "Вход и регистрация".

📝 test_registration.py
Тесты регистрации:
✅ Успешная регистрация с уникальными данными.
❌ Проверка невалидных email (через параметризацию).
🔁 Повторная регистрация с уже существующим пользователем.
Все ошибки проверяются через появление сообщения "Ошибка" и подсветку полей.

📢 test_create_an_ad.py
Проверка функциональности размещения объявления:
🔒 Неавторизованный пользователь видит сообщение об авторизации.
✅ Авторизованный пользователь может:
Заполнить форму объявления.
Выбрать город, категорию, состояние.
Опубликовать.
Проверить, что объявление появилось в профиле.

## Запуск тестов

Перед запуском укажите данные пользователя через переменные окружения `QA_EMAIL` и `QA_PASSWORD`:

```bash
export QA_EMAIL="your@mail.com"
export QA_PASSWORD="your_password"
pytest -q
```

Для запуска в безголовом режиме установите переменную `HEADLESS=1` (значение по умолчанию).

## Рекомендации

Тесты используют Selenium WebDriver и требуют установленного ChromeDriver.
