from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/redirect_accept.html"

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    # запускаем браузер
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_css_selector("button").click()

    # ищем значение Х и подставляем в формулу + записываем это значение в переменную У
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = browser.find_element_by_css_selector('#input_value').text
    y = calc(x)
    browser.find_element_by_css_selector("input#answer.form-control").send_keys(y)
    # ищем поле и вводим значение

    # Нажимаем на кнопку Submit.
    button = browser.find_element_by_css_selector(".btn").click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()