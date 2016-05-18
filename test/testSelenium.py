import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class testSelenium(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def wait(self):
    	time.sleep(2)

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5000")
        self.wait()
        add_user = driver.find_element_by_id("buttonC")
        add_user.click()
        self.wait()

		# AGREGAR USUARIO #
        name = driver.find_element_by_id("name")
        name.send_keys("Pedro")
        last_name = driver.find_element_by_id("last_name")
        last_name.send_keys("Perez")
        ci = driver.find_element_by_id("ci")
        ci.send_keys("12345678")
        email = driver.find_element_by_id("email")
        email.send_keys("correo@ejemplo.com")
        self.wait()
        email.submit()
        self.wait()
        
		# MOSTRAR USUARIOS #
        driver.get("http://127.0.0.1:5000")
        self.wait()
        driver.get("http://127.0.0.1:5000/users")
        self.wait()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()