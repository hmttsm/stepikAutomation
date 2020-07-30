from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
	link = "http://suninjuly.github.io/math.html"
	browser = webdriver.Chrome()
	browser.get(link)
	
	x_element = browser.find_element_by_css_selector("#input_value")
	x = x_element.text
	y = calc(x)
	
	answer = browser.find_element_by_css_selector("#answer")
	answer.send_keys(y)
	
	robot_checkbox = browser.find_element_by_css_selector("#robotCheckbox")
	robot_checkbox.click()
	
	robots_radiobutton = browser.find_element_by_css_selector("#robotsRule")
	robots_radiobutton.click()
	
	submit_button = browser.find_element_by_css_selector("button.btn")
	submit_button.click()

finally:
	time.sleep(3)
	browser.quit()

