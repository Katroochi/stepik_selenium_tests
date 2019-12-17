from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

def calc():
    return str(int(z) + int(y))


try:
    browser = webdriver.Chrome()
    #browser.get("http://suninjuly.github.io/selects1.html")
    browser.get("http://suninjuly.github.io/selects2.html")
    z = browser.find_element_by_id('num1').text
    y = browser.find_element_by_id('num2').text
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(calc())
    button = browser.find_element_by_class_name("btn.btn-default").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()