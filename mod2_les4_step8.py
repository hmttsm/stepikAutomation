from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
	link = "http://suninjuly.github.io/explicit_wait2.html"
	browser = webdriver.Chrome()
	browser.get(link)

	wait = WebDriverWait(browser, 12)
	wait.until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
	
	book_button = browser.find_element_by_css_selector("#book")
	book_button.click()
	
	browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
	
	x_element = browser.find_element_by_css_selector("#input_value")
	x = x_element.text
	answer = calc(x)
	
	answer_field = browser.find_element_by_css_selector("input.form-control#answer")
	answer_field.send_keys(answer)
	
	submit_button = browser.find_element_by_css_selector("#solve")
	submit_button.click()
	
	alert = browser.switch_to.alert
	alert_text = alert.text
	print(alert_text)
	
	
	
finally:
	time.sleep(5)
	browser.quit()