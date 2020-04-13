'''
Задание: оформляем тесты в стиле unittest 
Попробуйте оформить тесты из первого модуля в стиле unittest.
Возьмите тесты из шага - https://stepik.org/lesson/138920/step/11?unit=196194
Создайте новый файл
Создайте в нем класс с тестами, который должен наследоваться от unittest.TestCase по аналогии с предыдущим шагом
Перепишите в стиле unittest тест для страницы http://suninjuly.github.io/registration1.html
Перепишите в стиле unittest второй тест для страницы http://suninjuly.github.io/registration2.html
Оформите финальные проверки в тестах в стиле unittest, например, используя проверочный метод assertEqual
Запустите получившиеся тесты из файла 
Просмотрите отчёт о запуске и найдите последнюю строчку 
Отправьте эту строчку в качестве ответа на это задание 
Обратите внимание, что по задумке должно выбрасываться исключение NoSuchElementException во втором тесте. Если вы использовали конструкцию try/except, здесь нужно запустить тест без неё. Ловить исключения не надо (во всяком случае, здесь)!
Это всё для иллюстрации того, что unittest выполнит тесты и обобщит результаты даже при наличии неожиданного исключения. 
Не удаляйте код после прохождения этого задания, он пригодится в следующем уроке. 
'''

import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TestUnit(unittest.TestCase):
    def test_unit1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        elements = set([
            'Input your first name',
            'Input your last name',
            'Input your email',
        ])
        for element in elements:
            input1 = browser.find_element(By.CSS_SELECTOR,
                                          f'input[placeholder=\'{element}\']')
            input1.send_keys("test")
        # Отправляем заполненную форму.
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        # Находим элемент ожидая загрузки станицы, содержащий текст.
        welcome_text_elt = WebDriverWait(browser, 3).until(
            EC.presence_of_element_located((By.TAG_NAME, "h1")))
        # Записываем в переменную welcome_text текст из элемента welcome_text_elt.
        welcome_text = welcome_text_elt.text
        # Проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!",
                         welcome_text)
        # Закрываем браузер после всех манипуляций
        browser.quit()

    def test_unit2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        elements = set([
            'Input your first name',
            'Input your last name',
            'Input your email',
        ])
        for element in elements:
            input1 = browser.find_element(By.CSS_SELECTOR,
                                          f'input[placeholder=\'{element}\']')
            input1.send_keys("test")
        # Отправляем заполненную форму.
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        # Находим элемент ожидая загрузки станицы, содержащий текст.
        welcome_text_elt = WebDriverWait(browser, 3).until(
            EC.presence_of_element_located((By.TAG_NAME, "h1")))
        # Записываем в переменную welcome_text текст из элемента welcome_text_elt.
        welcome_text = welcome_text_elt.text
        # Проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!",
                         welcome_text)
        # Закрываем браузер после всех манипуляций
        browser.quit()


if __name__ == "__main__":
    unittest.main()
