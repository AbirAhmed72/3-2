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

class TestAllerrorstogether():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_allerrorstogether(self):
    # Test name: all errors together
    # Step # | name | target | value
    # 1 | open | / | 
    self.driver.get("https://leetcode.com/")
    # 2 | setWindowSize | 1920x1053 | 
    self.driver.set_window_size(1920, 1053)
    # 3 | click | linkText=Create Account | 
    self.driver.find_element(By.LINK_TEXT, "Create Account").click()
    # 4 | click | name=username | 
    self.driver.find_element(By.NAME, "username").click()
    # 5 | type | name=username | a
    self.driver.find_element(By.NAME, "username").send_keys("a")
    # 6 | click | name=password1 | 
    self.driver.find_element(By.NAME, "password1").click()
    # 7 | type | name=password1 | a
    self.driver.find_element(By.NAME, "password1").send_keys("a")
    # 8 | mouseDown | name=password2 | 
    element = self.driver.find_element(By.NAME, "password2")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 9 | mouseUp | css=.error-message-container__msvN:nth-child(4) | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".error-message-container__msvN:nth-child(4)")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    # 10 | click | css=.form__2-sN | 
    self.driver.find_element(By.CSS_SELECTOR, ".form__2-sN").click()
    # 11 | type | name=password2 | a
    self.driver.find_element(By.NAME, "password2").send_keys("a")
    # 12 | click | name=email | 
    self.driver.find_element(By.NAME, "email").click()
    # 13 | type | name=email | a
    self.driver.find_element(By.NAME, "email").send_keys("a")
    # 14 | mouseDown | name=signup_btn | 
    element = self.driver.find_element(By.NAME, "signup_btn")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 15 | mouseUp | css=.btn-content-container__2HVS | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".btn-content-container__2HVS")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    # 16 | click | name=signup_btn | 
    self.driver.find_element(By.NAME, "signup_btn").click()
    # 17 | click | name=password2 | 
    self.driver.find_element(By.NAME, "password2").click()
    # 18 | type | name=password2 | ab
    self.driver.find_element(By.NAME, "password2").send_keys("ab")
    # 19 | mouseDown | css=.btn-content-container__2HVS | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".btn-content-container__2HVS")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 20 | mouseUp | css=.error-message-container__msvN:nth-child(8) | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".error-message-container__msvN:nth-child(8)")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    # 21 | click | css=.container__1Q_2 | 
    self.driver.find_element(By.CSS_SELECTOR, ".container__1Q_2").click()
    # 22 | assertText | css=.error-message-container__msvN:nth-child(2) > .error-message__3Q-C | Content is too short
    assert self.driver.find_element(By.CSS_SELECTOR, ".error-message-container__msvN:nth-child(2) > .error-message__3Q-C").text == "Content is too short"
    # 23 | assertText | css=.error-message-container__msvN:nth-child(4) > .error-message__3Q-C | Must be 8 characters or more, needs at least one number and one letter
    assert self.driver.find_element(By.CSS_SELECTOR, ".error-message-container__msvN:nth-child(4) > .error-message__3Q-C").text == "Must be 8 characters or more, needs at least one number and one letter"
    # 24 | assertText | css=.error-message-container__msvN:nth-child(6) > .error-message__3Q-C | The passwords you entered do not match.
    assert self.driver.find_element(By.CSS_SELECTOR, ".error-message-container__msvN:nth-child(6) > .error-message__3Q-C").text == "The passwords you entered do not match."
    # 25 | assertText | css=.error-message-container__msvN:nth-child(8) > .error-message__3Q-C | Invalid email address
    assert self.driver.find_element(By.CSS_SELECTOR, ".error-message-container__msvN:nth-child(8) > .error-message__3Q-C").text == "Invalid email address"
  
