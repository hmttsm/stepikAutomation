from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
try:
	link = "http://suninjuly.github.io/execute_script.html"
	browser = webdriver.Chrome()
	browser.get(link)
	
	x_element = browser.find_element_by_css_selector("#input_value")
	x = x_element.text
	answer = calc(x)
	
	browser.execute_script("window.scrollBy(0, 150);")
	
	answer_field = browser.find_element_by_css_selector("#answer.form-control")
	answer_field.send_keys(answer)
	
	robot_checkbox = browser.find_element_by_css_selector("#robotCheckbox")
	robot_checkbox.click()
	
	robots_radiobutton = browser.find_element_by_css_selector("#robotsRule")
	robots_radiobutton.click()
	
	submit_button = browser.find_element_by_css_selector("button.btn")
	submit_button.click()
	
finally:
	time.sleep(7)
	browser.quit()
	