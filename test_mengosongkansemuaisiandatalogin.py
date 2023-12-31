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

class TestMengosongkansemuaisiandatalogin():
  def setup_method(self, method):
    self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_mengosongkansemuaisiandatalogin(self):
    # Test name: Mengosongkan semua isian data login
    # Step # | name | target | value
    # 1 | open | / | 
    self.driver.get("https://www.facebook.com/")
    # 2 | setWindowSize | 656x680 | 
    self.driver.set_window_size(656, 680)
    # 3 | click | id=u_0_5_Cd | 
    self.driver.find_element(By.ID, "u_0_5_Cd").click()
    # 4 | assertText | css=.fsl | Wrong credentials
    assert self.driver.find_element(By.CSS_SELECTOR, ".fsl").text == "Wrong credentials"
    # 5 | close |  | 
    self.driver.close()
  
