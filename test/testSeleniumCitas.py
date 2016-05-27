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

        # AGREGAR USUARIO DE PRUEBA#
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
        role =driver.find_element_by_id("role")
        role.click()
        self.wait()
        email.submit()
        self.wait()

        # LOGIN #
        login = driver.find_element_by_name("username")
        login.send_keys("pperez")
        passw = driver.find_element_by_name("password")
        passw.send_keys("1234")
        passw.submit()
        self.wait()

        #CITAS#
        #Agregar Cita#
        appointments = driver.find_element_by_xpath('//a[@href="/appointments"]')
        appointments.click()
        self.wait()
        add_appointment = driver.find_element_by_xpath('//a[@href="/add_appointment"]')
        add_appointment.click()
        self.wait()
        add_date = driver.find_element_by_xpath('//input[@id="date"]')
        add_date.send_keys("2016-05-30")
        self.wait()
        add_description = driver.find_element_by_id("description")
        add_description.send_keys("descripcion ejemplo cita")
        self.wait()
        add_description.submit()
        self.wait()

        #Modificar Cita#
        edit_appointment = driver.find_element_by_xpath('//a[@href="/modify_appointment/8"]')
        edit_appointment.click()
        self.wait()
        edit_date = driver.find_element_by_xpath('//input[@id="date"]')
        edit_date.clear()
        self.wait()
        edit_date.send_keys("2016-06-15")
        self.wait()
        edit_description = driver.find_element_by_id("description")
        edit_description.clear()
        self.wait()
        edit_description.send_keys("descripcion modificada")
        self.wait()
        edit_description.submit()
        self.wait()

        #Eliminar Cita#
        delete_appointment = driver.find_element_by_xpath("//button[@onclick='openModal(8)']") #Cita previamente modificada
        delete_appointment.click()
        self.wait()
        delete_appointment = driver.find_element_by_id("deleteButton_appointment")
        delete_appointment.click()
        self.wait()

        driver.get("http://127.0.0.1:5000/users")
        self.wait()

        #Agregar Role#
        add_role = driver.find_element_by_xpath("//button[@id='show-add-role']")
        add_role.click()
        self.wait()
        add = driver.find_element_by_xpath("//input[@id='role']")
        add.send_keys("Rol Nuevo")
        self.wait()
        add_role = driver.find_element_by_xpath("//button[@id='add-role']")
        add_role.click()
        #AQUI ESTA OCURRIENDO UN FALLO#
        driver.get("http://127.0.0.1:5000/users")
        self.wait()


        

        # SALIR #
        exit = driver.find_element_by_xpath('//a[@href="/logout"]')
        exit.click()
        self.wait()

        #Verificar creacion de rol#
        add_user = driver.find_element_by_id("registrarse")
        add_user.click()    
        self.wait()

        ci = driver.find_element_by_id("ci")
        ci.send_keys("5678")
        user_name = driver.find_element_by_id("username")
        user_name.send_keys("jgonzalez")
        password = driver.find_element_by_id("password")
        password.send_keys("1234")
        name = driver.find_element_by_id("name")
        name.send_keys("Jose")
        last_name = driver.find_element_by_id("last_name")
        last_name.send_keys("Gonzalez")
        email = driver.find_element_by_id("email")
        email.send_keys("correo2@ejemplo.com")
        self.wait()
        role =driver.find_element_by_id("role")
        role.click()
        self.wait()
        role = driver.find_element_by_xpath('//option[@value="4"]')
        role.click()
        self.wait()
        role =driver.find_element_by_id("role")
        role.submit()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()