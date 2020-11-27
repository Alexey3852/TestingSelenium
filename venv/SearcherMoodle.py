import time  # Library for time-working
from selenium import webdriver  # Import webdriver for browser control
my_password = "rb26dett"
driver = webdriver.Chrome()   # Initialize browser driver
driver.get("https://portal.edu.asu.ru/")
driver.find_element_by_link_text('Вход').click()
driver.find_element_by_id('username').send_keys('Busova.1397m@stud.asu.ru')
driver.find_element_by_id('password').send_keys(my_password)
time.sleep(15)
driver.find_element_by_id('loginbtn').click()

driver.find_element_by_id('shortsearchbox').send_keys('Журенков')
time.sleep(15)
driver.find_element_by_class_name('btn-secondary').submit()