'''
Задание: принимаем alert
В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:
Открыть страницу http://suninjuly.github.io/alert_accept.html
Нажать на кнопку
Принять confirm
На новой странице решить капчу для роботов, чтобы получить число с ответом
Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), вы увидите окно с числом. Отправьте полученное число в качестве ответа на это задание.
'''


import math
import time

from selenium import webdriver

try:
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Нажать на кнопку.
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Переключаюсь на алерт.
    alert = browser.switch_to.alert
    # Соглашаюсь с ним(нажимая на кнопку).
    alert.accept()

    # Нахожу число и запускаю функцию расчета.
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    # Нахожу поле и заполняю его ответом из расчета.
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)

    # Отправляем заполненную форму(нажатием кнопки)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit
