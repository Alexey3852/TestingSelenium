import time  # Library for time-working
from selenium import webdriver  # Import webdriver for browser control

driver = webdriver.Chrome()   # Initialize browser driver
driver.get("https://yandex.ru/")

x = driver.find_element_by_name("text")
x.send_keys('Есть ли жизнь на Марсе?')
time.sleep(20)
x.submit()
