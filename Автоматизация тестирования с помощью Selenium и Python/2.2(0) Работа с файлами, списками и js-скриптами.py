'''
Задание: работа с выпадающим списком
Для этой задачи мы придумали еще один вариант капчи для роботов. Придется немного переобучить нашего робота, чтобы он справился с новым заданием.
Напишите код, который реализует следующий сценарий:
Открыть страницу http://suninjuly.github.io/selects1.html
Посчитать сумму заданных чисел
Выбрать в выпадающем списке значение равное расчитанной сумме
Нажать кнопку "Submit"
Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), вы увидите окно с числом. Отправьте полученное число в качестве ответа для этого задания.
Когда ваш код заработает, попробуйте запустить его на странице http://suninjuly.github.io/selects2.html. Ваш код и для нее тоже ﻿должен пройти успешно.
Подсказка: если вы получаете ошибку в духе "argument of type 'int' is not iterable", перепроверьте тип переменной, которую вы передаете в функцию поиска. Нужно передать строку! 
'''


from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:

    link = "http://suninjuly.github.io/selects2.html"

    browser = webdriver.Chrome()
    browser.get(link)

    # Нахожу значения из ячеек и складываю их
    x = browser.find_element_by_id('num1')
    x = int(x.text)
    y = browser.find_element_by_id('num2')
    y = int(y.text)
    summ = str(x + y)
    # Нахожу выпадающий список и ищу в нем элемент(выбираю его)
    select = Select(browser.find_element_by_id('dropdown'))
    select.select_by_visible_text(summ)  # ищем элемент с текстом

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
