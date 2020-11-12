from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time
import math
	
#def findElement()
#	return browser.find_element_by_css_selector("")
	
@pytest.fixture(scope="class")
def answer():
	return str(math.log(int(time.time())))

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

class TestToFindString():

#		links = [
#		("https://stepik.org/lesson/236895/step/1"),
#		("https://stepik.org/lesson/236896/step/1"),
	#	("https://stepik.org/lesson/236897/step/1"),
	#	("https://stepik.org/lesson/236898/step/1"),
	#	("https://stepik.org/lesson/236899/step/1"),
	#	("https://stepik.org/lesson/236903/step/1"),
	#	("https://stepik.org/lesson/236904/step/1"),
	#	("https://stepik.org/lesson/236905/step/1")]
		
		@pytest.mark.parametrize('links', ["236895", "236896", "236899", "236897", "236898", "236903", "236904", "236904"])
		def test(self, browser, answer, links):
			link = f"https://stepik.org/lesson/{links}/step/1"
			browser.get(link)
			wait = WebDriverWait(browser, 5)
			answer_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.textarea')))
			answer_field.send_keys(answer)
			print(answer)
		
		
	
	


