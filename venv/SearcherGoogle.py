import time  # Library for time-working
from selenium import webdriver  # Import webdriver for browser control

driver = webdriver.Chrome()   # Initialize browser driver
driver.get("https://google.com/")


x = driver.find_element_by_css_selector('.gLFyf')
x.send_keys('Есть ли жизнь на Марсе?')
x.submit()
