# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import xmlrunner
import mysql.connector

class IDWithWrongFormatSalary(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://192.168.135.128"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_id_with_wrong_format_salary(self):
        driver = self.driver
        driver.get(self.base_url + "/phptest.php")
        driver.find_element_by_id("emp_id").clear()
        driver.find_element_by_id("emp_id").send_keys("Testing1")
        driver.find_element_by_id("emp_salary").clear()
        driver.find_element_by_id("emp_salary").send_keys("abc")
        driver.find_element_by_id("update").click()
        self.assertEqual("Empolyer salary is not a number.", driver.find_element_by_css_selector("p").text)

    def test_id_without_salary(self):
        driver = self.driver
        driver.get(self.base_url + "/phptest.php")
        driver.find_element_by_id("emp_id").clear()
        driver.find_element_by_id("emp_id").send_keys("Testing1")
        driver.find_element_by_id("emp_salary").clear()
        driver.find_element_by_id("update").click()
        self.assertEqual("Empolyer salary is not a number.", driver.find_element_by_css_selector("p").text)

    def test_no_id_no_salary(self):
        driver = self.driver
        driver.get(self.base_url + "/phptest.php")
        driver.find_element_by_id("emp_id").clear()
        driver.find_element_by_id("emp_salary").clear()
        driver.find_element_by_id("update").click()
        self.assertEqual("Please enter Empolyer ID.", driver.find_element_by_css_selector("p").text)
    
    def test_insert_id_salary(self):

        cnx = mysql.connector.connect(user='phpadmin', password='phpadmin', host='localhost', database='phptest')
        cursor = cnx.cursor()
        query = "DELETE FROM employee WHERE emp_id = 'Testing1' and emp_salary=10000;"
        cursor.execute(query)
        cnx.commit()
        
        driver = self.driver
        emp_id = "Testing1"
        emp_salary=10000
        driver.get(self.base_url + "/phptest.php")
        driver.find_element_by_id("emp_id").clear()
        driver.find_element_by_id("emp_id").send_keys("Testing1")
        driver.find_element_by_id("emp_salary").clear()
        driver.find_element_by_id("emp_salary").send_keys("10000")

        driver.find_element_by_id("update").click()
        time.sleep(1)
        query = "Select COUNT(*) as total FROM employee WHERE emp_id = 'Testing1' and emp_salary=10000;"
        cursor.execute(query)
        row = cursor.fetchone()
        self.assertEqual(1,row[0])

        query = "DELETE FROM employee WHERE emp_id = 'Testing1' and emp_salary=10000;"
        cursor.execute(query)
        cnx.commit()

        cursor.close()
        cnx.close()
    '''
    def test_delete_id_delete_salary(self):
        driver = self.driver
        emp_id = "Testing1"
        emp_salary=10000
        driver.get(self.base_url + "/phptest.php")
        driver.find_element_by_id("emp_id").clear()
        driver.find_element_by_id("emp_id").send_keys("Testing1")
        driver.find_element_by_id("emp_salary").clear()
        driver.find_element_by_id("emp_salary").send_keys("10000")
        driver.find_element_by_id("update").click()
        cnx = mysql.connector.connect(user='phpadmin', password='phpadmin', host='localhost', database='phptest')
        cursor = cnx.cursor()

        query = "Select COUNT(*) as total FROM employee WHERE emp_id = 'Testing1' and emp_salary=10000;"
        cursor.execute(query)
        row = cursor.fetchone()
        self.assertEqual(1,row[0])
        cursor.close()
        cnx.close()
    '''
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
	with open('phpWebTestResults.xml', 'wb') as output:
    		unittest.main(testRunner=xmlrunner.XMLTestRunner(output=output))

