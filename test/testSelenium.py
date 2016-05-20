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
        add_user = driver.find_element_by_id("registrarse")
        add_user.click()    
        self.wait()

        # AGREGAR USUARIO #
        ci = driver.find_element_by_id("ci")
        ci.send_keys("12345678")
        user_name = driver.find_element_by_id("username")
        user_name.send_keys("pperez")
        password = driver.find_element_by_id("password")
        password.send_keys("1234")
        name = driver.find_element_by_id("name")
        name.send_keys("Pedro")
        last_name = driver.find_element_by_id("last_name")
        last_name.send_keys("Perez")
        email = driver.find_element_by_id("email")
        email.send_keys("correo@ejemplo.com")
        self.wait()
        email.submit()
        self.wait()

        # LOGIN #
        login = driver.find_element_by_name("username")
        login.send_keys("pperez")
        passw = driver.find_element_by_name("password")
        passw.send_keys("1234")
        passw.submit()

        # MODIFICAR USUARIO #
        modify_user = driver.find_element_by_xpath('//a[@href="/modify_user/12345678"]')#Usuario recientemente anadido
        modify_user.click()
        self.wait()
        name = driver.find_element_by_id("name")
        name.send_keys(" Jose")
        last_name = driver.find_element_by_id("last_name")
        last_name.send_keys(" Gonzalez")
        email = driver.find_element_by_id("email")
        email.clear()
        email.send_keys("pedroperez@ejemplo.com")
        self.wait()
        email.submit()
        self.wait()

        # ELIMINAR USUARIO#
        delete_user = driver.find_element_by_xpath('//button[@id="delete_user"]')#Usuario previamente modificado
        delete_user.click()
        self.wait()
        delete_user = driver.find_element_by_id("deleteButton")
        delete_user.click()
        self.wait()

       # /html/body/div[2]/div[@class='container']/div[@id='cuerpoHeredado']/table/tbody/tr[@id='12345678']/td[7]/button[@id='delete_user']/i[@class='fa fa-trash']
       #/html/body/div[2]/div[@class='container']/div[@id='cuerpoHeredado']/table/tbody/tr[@id='12345678']/td[7]/button[@id='delete_user']/i[@class='fa fa-trash']

        # MOSTRAR USUARIOS #
        driver.get("http://127.0.0.1:5000")
        self.wait()
        driver.get("http://127.0.0.1:5000/users")
        self.wait()

        # SALIR #
        exit = driver.find_element_by_link_text("Salir")
        exit.click()
        self.wait()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()