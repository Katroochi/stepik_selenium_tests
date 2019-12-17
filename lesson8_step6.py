import math
from selenium import webdriver
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(" http://suninjuly.github.io/alert_accept.html")
    button = browser.find_element_by_class_name("btn.btn-primary").click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    browser.execute_script("window.scrollBy(0, 100);")
    end = browser.find_element_by_id("answer").send_keys(calc(x))
    check = browser.find_element_by_id("robotCheckbox").click()
    radio = browser.find_element_by_css_selector("[for = 'robotsRule']").click()
    buttonSubmit = browser.find_element_by_class_name("btn.btn-primary").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()
