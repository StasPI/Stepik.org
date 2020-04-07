'''
Задание: поиск сокровища с помощью get_attribute
В данной задаче вам нужно с помощью роботов решить ту же математическую задачу, как и в прошлом задании. Но теперь значение переменной х спрятано в "сундуке", точнее, значение хранится в атрибуте valuex у картинки с изображением сундука.
Ваша программа должна:
Открыть страницу http://suninjuly.github.io/get_attribute.html.
Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
Посчитать математическую функцию от x (сама функция остаётся неизменной).
Ввести ответ в текстовое поле.
Отметить checkbox "I'm the robot".
Выбрать radiobutton "Robots rule!".
Нажать на кнопку "Submit".
Для вычисления значения выражения в п.4 используйте функцию calc(x) из предыдущей задачи.
Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), вы увидите окно с числом. Скопируйте его в поле ниже и нажмите кнопку "Submit", чтобы получить баллы за задание.
'''


from selenium import webdriver
import time
import math

try:
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    link = "http://suninjuly.github.io/get_attribute.html"

    browser = webdriver.Chrome()
    browser.get(link)
    # Нахожу число и запускаю функцию расчета.
    x_element = browser.find_element_by_css_selector('.container img')
    x = x_element.get_attribute('valuex')
    y = calc(x)
    # Нахожу поле и заполняю его ответом из расчета.
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    # Нахожу чекбокс и наживаю на его.
    input_checkbox1 = browser.find_element_by_id('robotCheckbox')
    input_checkbox1.click()
    # Нахожу радио кнопку и переключаю на нужный пункт.
    input_radio1 = browser.find_element_by_id('robotsRule')
    input_radio1.click()
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
