import math
from selenium import webdriver
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")
    x_element = browser.find_element_by_id('treasure').get_attribute("valuex")
    x = x_element
    y = calc(x)
    end = browser.find_element_by_id("answer").send_keys(calc(x))
    check = browser.find_element_by_id("robotCheckbox").click()
    radio = browser.find_element_by_id("robotsRule").click()
    button = browser.find_element_by_class_name("btn.btn-default").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
