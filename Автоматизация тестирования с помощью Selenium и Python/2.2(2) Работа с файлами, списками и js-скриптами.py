'''
Задание: загрузка файла
В этом задании в форме регистрации требуется загрузить текстовый файл.

Напишите скрипт, который будет выполнять следующий сценарий:

Открыть страницу http://suninjuly.github.io/file_input.html
Заполнить текстовые поля: имя, фамилия, email
Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
Нажать кнопку "Submit"
Если все сделано правильно и быстро, вы увидите окно с числом. Отправьте полученное число в качестве ответа для этого задания.
'''


import math
import os
import time

from selenium import webdriver

try:

    # Получаем путь к директории текущего исполняемого файла.
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # Добавляем к этому пути имя файла.
    file_path = os.path.join(current_dir, 'file.txt')

    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    elements = [
        'firstname',
        'lastname',
        'email',
    ]
    # Перебираем и заполняем необходимые поля.
    for element in elements:
        input1 = browser.find_element_by_name(element)
        input1.send_keys("test")

    # Находим кнопку загрузки файла и грузим файл(передаем адрес файла).
    file1 = browser.find_element_by_id('file')
    file1.send_keys(file_path)
    # Отправляем заполненную форму
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit
