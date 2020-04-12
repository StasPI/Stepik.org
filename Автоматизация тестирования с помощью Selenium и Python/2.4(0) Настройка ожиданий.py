'''
Задание: ждем нужный текст на странице
Попробуем теперь написать программу, которая будет бронировать нам дом для отдыха по строго заданной цене. Более высокая цена нас не устраивает, а по более низкой цене объект успеет забронировать кто-то другой.
В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:
Открыть страницу http://suninjuly.github.io/explicit_wait2.html
Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
Нажать на кнопку "Book"
Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
Чтобы определить момент, когда цена аренды уменьшится до $100, используйте метод text_to_be_present_in_element из библиотеки expected_conditions.
Если все сделано правильно и быстро, то вы увидите окно с числом. Отправьте его в качестве ответа на это задание.
'''


import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    # Проверяю цену в течении 12 секунд пока она не совпадет с искомым значением $100, как только совпадает ищу и нажимаю на кнопку бронировать.
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    button_book = browser.find_element(By.ID, 'book')
    button_book.click()
    # Поиск и расчет значения.
    value = browser.find_element(By.ID, 'input_value')
    value = value.text
    value = calc(value)
    # Поиск и добавление информации в поле.
    input_value = browser.find_element(By.ID, 'answer')
    input_value.send_keys(value)
    # Отправка формы.
    button_submit = browser.find_element(By.ID, 'solve')
    button_submit.click()
finally:
    # Ожидание чтобы визуально оценить результаты прохождения скрипта.
    time.sleep(10)
    # Закрываем браузер после всех манипуляций.
    browser.quit
