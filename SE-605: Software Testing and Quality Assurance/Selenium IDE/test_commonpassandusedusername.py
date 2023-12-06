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

class TestCommonpassandusedusername():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_commonpassandusedusername(self):
    # Test name: common pass and used username
    # Step # | name | target | value
    # 1 | open | / | 
    self.driver.get("https://leetcode.com/")
    # 2 | setWindowSize | 1920x1053 | 
    self.driver.set_window_size(1920, 1053)
    # 3 | click | linkText=Create Account | 
    self.driver.find_element(By.LINK_TEXT, "Create Account").click()
    # 4 | click | name=username | 
    self.driver.find_element(By.NAME, "username").click()
    # 5 | type | name=username | test2
    self.driver.find_element(By.NAME, "username").send_keys("test2")
    # 6 | click | name=password1 | 
    self.driver.find_element(By.NAME, "password1").click()
    # 7 | doubleClick | name=password1 | 
    element = self.driver.find_element(By.NAME, "password1")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    # 8 | type | name=password1 | a12345678
    self.driver.find_element(By.NAME, "password1").send_keys("a12345678")
    # 9 | click | name=password2 | 
    self.driver.find_element(By.NAME, "password2").click()
    # 10 | type | name=password2 | a12345678
    self.driver.find_element(By.NAME, "password2").send_keys("a12345678")
    # 11 | click | name=email | 
    self.driver.find_element(By.NAME, "email").click()
    # 12 | type | name=email | abir@gmail.com
    self.driver.find_element(By.NAME, "email").send_keys("abir@gmail.com")
    # 13 | click | css=.btn-content-container__2HVS | 
    self.driver.find_element(By.CSS_SELECTOR, ".btn-content-container__2HVS").click()
    # 14 | assertText | css=.error-message-container__msvN:nth-child(4) > .error-message__3Q-C | This password is too common.
    assert self.driver.find_element(By.CSS_SELECTOR, ".error-message-container__msvN:nth-child(4) > .error-message__3Q-C").text == "This password is too common."
    # 15 | assertText | css=.error-message-container__msvN:nth-child(2) > .error-message__3Q-C | Username cannot be used. Please choose another username.
    assert self.driver.find_element(By.CSS_SELECTOR, ".error-message-container__msvN:nth-child(2) > .error-message__3Q-C").text == "Username cannot be used. Please choose another username."
  