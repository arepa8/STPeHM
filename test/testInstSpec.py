import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class testInstSpec(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Firefox()

	def wait(self):
		time.sleep(2)

	def testInstSpec(self):
		driver = self.driver
		driver.get("http://127.0.0.1:5000")
		self.wait()

		# LOGIN #
		login = driver.find_element_by_name("username")
		login.send_keys("admin")
		passw = driver.find_element_by_name("password")
		passw.send_keys("admin")
		passw.submit()
		self.wait()

		# INSTITUTION #
		add_institutions = driver.find_element_by_xpath('//a[@href="/add_institution"]')
		add_institutions.click()
		self.wait()
		name = driver.find_element_by_xpath('//input[@id="name"]')
		name.send_keys("Clinicas Caracas")
		address = driver.find_element_by_xpath('//input[@id="address"]')
		address.send_keys("Aqui")
		address.submit()
		self.wait()

		modify = driver.find_element_by_xpath('//a[@href="/modify_institution/1"]')
		modify.click()
		self.wait()
		name = driver.find_element_by_xpath('//input[@id="name"]')
		name.send_keys("")
		name.send_keys("Clinica El Avila")
		address = driver.find_element_by_xpath('//input[@id="address"]')
		address.send_keys("")
		address.send_keys("Alla")
		address.submit()
		self.wait()

		delete = driver.find_element_by_xpath('//button[@onclick="openModal_institution(1)"]')
		delete.click()
		delete = driver.find_element_by_id("deleteButton_institution")
		delete.click()
		self.wait()
		
		# SPECIALIZATION # 

		add_specializations = driver.find_element_by_xpath('//a[@href="/add_specialization"]')
		add_specializations.click()
		self.wait()
		name = driver.find_element_by_xpath('//input[@id="name"]')
		name.send_keys("Traumatologia")
		name.submit()
		self.wait()

		modify = driver.find_element_by_xpath('//a[@href="/modify_specialization/1"]')
		modify.click()
		self.wait()
		name = driver.find_element_by_xpath('//input[@id="name"]')
		name.send_keys("")
		name.send_keys("Oftalmologia")
		name.submit()

		delete = driver.find_element_by_xpath('//button[@onclick="openModal_specialization(1)"]')
		delete.click()
		delete = driver.find_element_by_id("deleteButton_specialization")
		delete.click()
		self.wait()

		def tearDown(self):
			self.driver.close()

if __name__ == '__main__':
	unittest.main()