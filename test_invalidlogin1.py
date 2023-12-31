# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from constants import globalConstants as c

class TestInvalidlogin1():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_invalidlogin1(self):
    self.driver.get(c.BASE_URL)
    self.driver.set_window_size(1552, 840)
    self.driver.find_element(By.ID, c.USERNAME_ID).click()
    self.driver.find_element(By.ID, c.PASSWORD_ID).click()
    self.driver.find_element(By.ID, c.LOGIN_BUTTON_ID).click()
    assert self.driver.find_element(By.XPATH, "//h3[contains(.,\'Epic sadface: Username is required\')]").text == "Epic sadface: Username is required"
    self.driver.close()
  
