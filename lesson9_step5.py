import math
from selenium import webdriver
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    button = browser.find_element_by_class_name("trollface.btn.btn-primary").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    end = browser.find_element_by_id("answer").send_keys(calc(x))
    buttonSubmit = browser.find_element_by_class_name("btn.btn-primary").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()
