from selenium import webdriver
import time
import os

try:
	link = "http://suninjuly.github.io/file_input.html"
	browser = webdriver.Chrome()
	browser.get(link)
	
	first_name_field = browser.find_element_by_css_selector("[name='firstname']")
	first_name_field.send_keys("first name")
	last_name_field = browser.find_element_by_css_selector("[name='lastname']")
	last_name_field.send_keys("last name")
	email_field = browser.find_element_by_css_selector("[name='email']")
	email_field.send_keys("email")
	
	current_dir = os.path.abspath(os.path.dirname(__file__))
	file_path = os.path.join(current_dir, 'test.txt')
	upload_file = browser.find_element_by_css_selector("#file")
	upload_file.send_keys(file_path)
	
	submit_button = browser.find_element_by_css_selector("button.btn")
	submit_button.click()
	
finally:
	time.sleep(7)
	browser.quit()