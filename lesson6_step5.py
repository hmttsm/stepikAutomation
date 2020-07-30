from selenium import webdriver
import math

#open testing link
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/find_link_text")

#find hidden link text
hidden = str(math.ceil(math.pow(math.pi, math.e)*10000))

#open link by hidden link text
link = browser.find_element_by_link_text(hidden)
link.click()

#fill the form to get answer
input1 = browser.find_element_by_tag_name("input")
input1.send_keys("Ivan")
input2 = browser.find_element_by_name("last_name")
input2.send_keys("Petrov")
input3 = browser.find_element_by_class_name("city")
input3.send_keys("Smolensk")
input4 = browser.find_element_by_id("country")
input4.send_keys("Russia")
button = browser.find_element_by_css_selector("button.btn")
button.click()

time.sleep(10)
browser.quit()
