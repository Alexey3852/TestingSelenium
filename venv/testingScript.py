import time  # Library for time-working
from selenium import webdriver  # Import webdriver for browser control

driver = webdriver.Chrome()   # Initialize browser driver
time.sleep(10)
driver.get("https://portal.edu.asu.ru/")
time.sleep(10)
driver.quit()