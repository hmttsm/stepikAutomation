from selenium import webdriver
import time
import unittest

class TestUnittests(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome()
		
	def test_reg1(self):
		link = "http://suninjuly.github.io/registration1.html"
		browser = self.driver
		browser.get(link)
		# Ваш код, который заполняет обязательные поля
		first_name_field = browser.find_element_by_css_selector(".first_block .form-control.first")
		first_name_field.send_keys("a")
		second_name_field = browser.find_element_by_css_selector(".first_block .form-control.second")
		second_name_field.send_keys("b")
		third_name_field = browser.find_element_by_css_selector(".first_block .form-control.third")
		third_name_field.send_keys("c")
		# Отправляем заполненную форму
		button = browser.find_element_by_css_selector("button.btn")
		button.click()
		# Проверяем, что смогли зарегистрироваться
		# ждем загрузки страницы
		time.sleep(1)
		# находим элемент, содержащий текст
		welcome_text_elt = browser.find_element_by_tag_name("h1")
		# записываем в переменную welcome_text текст из элемента welcome_text_elt
		welcome_text = welcome_text_elt.text
		self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "something wrong. check the code!")
		
	def test_reg2(self):
		link = "http://suninjuly.github.io/registration2.html"
		browser = self.driver
		browser.get(link)
		# Ваш код, который заполняет обязательные поля
		first_name_field = browser.find_element_by_css_selector(".first_block .form-control.first")
		first_name_field.send_keys("a")
		second_name_field = browser.find_element_by_css_selector(".first_block .form-control.second")
		second_name_field.send_keys("b")
		third_name_field = browser.find_element_by_css_selector(".first_block .form-control.third")
		third_name_field.send_keys("c")
		# Отправляем заполненную форму
		button = browser.find_element_by_css_selector("button.btn")
		button.click()
		# Проверяем, что смогли зарегистрироваться
		# ждем загрузки страницы
		time.sleep(1)
		# находим элемент, содержащий текст
		welcome_text_elt = browser.find_element_by_tag_name("h1")
		# записываем в переменную welcome_text текст из элемента welcome_text_elt
		welcome_text = welcome_text_elt.text
		self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "something wrong. check the code!")
		
	def tearDown(self):
		self.driver.close()
		

if __name__ == "__main__":
    unittest.main()