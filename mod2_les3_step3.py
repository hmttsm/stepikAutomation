from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
	link = "http://suninjuly.github.io/alert_accept.html"
	browser = webdriver.Chrome()
	browser.get(link)
	
	button = browser.find_element_by_css_selector("button.btn")
	button.click()
	
	alert = browser.switch_to.alert
	alert.accept()
	
	x_element = browser.find_element_by_css_selector("#input_value")
	x = x_element.text
	y = calc(x)
	
	textbox = browser.find_element_by_css_selector("#answer")
	textbox.send_keys(y)
	
	submit_button = browser.find_element_by_css_selector("button.btn")
	submit_button.click()
	
finally:
	time.sleep(7)
	browser.quit()