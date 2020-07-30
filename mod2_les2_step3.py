from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
#import math

def sum(x,y):
  return int(x)+int(y)

try:
	link = "http://suninjuly.github.io/selects2.html"
	browser = webdriver.Chrome()
	browser.get(link)
	
	x_element = browser.find_element_by_css_selector("#num1")
	x = x_element.text
	y_element = browser.find_element_by_css_selector("#num2")
	y = y_element.text
	
	found_sum = str(sum(x,y))
	
	select = Select(browser.find_element_by_css_selector("#dropdown.custom-select"))
	select.select_by_visible_text(found_sum)
	
	submit_button = browser.find_element_by_css_selector("button.btn")
	submit_button.click()

finally:
	time.sleep(5)
	browser.quit()