'''
Задание: параметризация тестов
Инопланетяне оставляют загадочные сообщения на Stepik в фидбеке задач на правильное решение. Мы смогли локализовать несколько url-адресов задач, где появляются кусочки сообщений. Ваша задача - реализовать автотест со следующим сценарием действий: 
открыть страницу 
ввести правильный ответ 
нажать кнопку "Отправить" 
дождаться фидбека о том, что ответ правильный 
проверить, что текст в опциональном фидбеке полностью совпадает с "Correct!"
Опциональный фидбек — это текст в черном поле, как показано на скриншоте: 
Правильным ответом на задачу в заданных шагах является число 
import time
import math
answer = math.log(int(time.time()))
Используйте маркировку pytest для параметризации и передайте в тест список ссылок в качестве параметров: 
https://stepik.org/lesson/236895/step/1
https://stepik.org/lesson/236896/step/1
https://stepik.org/lesson/236897/step/1
https://stepik.org/lesson/236898/step/1
https://stepik.org/lesson/236899/step/1
https://stepik.org/lesson/236903/step/1
https://stepik.org/lesson/236904/step/1
https://stepik.org/lesson/236905/step/1
Используйте осмысленное сообщение об ошибке в проверке текста, а также настройте нужные ожидания, чтобы тесты работали стабильно. 
В упавших тестах найдите кусочки послания. Тест должен падать, если текст в опциональном фидбеке не совпадает со строкой "Correct!" Соберите кусочки текста в одно предложение и отправьте в качестве ответа на это задание. 
Важно! Чтобы пройти это задание, дополнительно убедитесь в том, что у вас установлено правильное локальное время (https://time.is/ru/). Ответ для каждой задачи нужно пересчитывать отдельно, иначе они устаревают. 
'''

import math
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


url_list = [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1',
]


@pytest.mark.parametrize('url', url_list)
def test_ufo(browser, url):
    link = url
    browser.get(link)
    answer = math.log(int(time.time()))
    # Ожидаем появление элемента на странице, находим его, заполняем форму, нажимаем отправить форму.
    input_value = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, 'ember69')))
    input_value.send_keys(str(answer))
    button = browser.find_element(By.CLASS_NAME, 'submit-submission')
    button.click()
    # Ожидаем поля обратной связи, изымаем его содержимое и проверяем асертом на соответствие заданному условию.
    feedback = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'smart-hints__hint')))
    feedback = feedback.text

    assert feedback == 'Correct!', 'no corrected!'
