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

class TestInvalidlog2():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_invalidlog2(self):
    self.driver.get("https://www.saucedemo.com/")
    self.driver.set_window_size(1552, 840)
    self.driver.find_element(By.ID, "user-name").click()
    self.driver.find_element(By.NAME, "user-name").send_keys("standard_user")
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.NAME, "password").send_keys("secret_sauce")
    self.driver.find_element(By.ID, "login-button").click()
    assert self.driver.find_element(By.XPATH, "//div[@id=\'header_container\']/div/div[2]/div").text == "Swag Labs"
    self.driver.get("https://www.saucedemo.com/")
    self.driver.find_element(By.ID, "user-name").click()
    self.driver.find_element(By.NAME, "user-name").send_keys("error_user")
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.NAME, "password").send_keys("secret_sauce")
    self.driver.find_element(By.ID, "login-button").click()
    assert self.driver.find_element(By.XPATH, "//div[@id=\'header_container\']/div/div[2]/div").text == "Swag Labs"
    self.driver.get("https://www.saucedemo.com/")
    self.driver.find_element(By.ID, "user-name").click()
    self.driver.find_element(By.NAME, "user-name").send_keys("visual_user")
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.NAME, "password").send_keys("secret_sauce")
    self.driver.find_element(By.ID, "login-button").click()
    assert self.driver.find_element(By.XPATH, "//div[@id=\'header_container\']/div/div[2]/div").text == "Swag Labs"
    self.driver.close()
  
