#!/usr/bin/python3
import time
import os
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

json_path = os.path.join(
    os.environ['USERPROFILE'],
    "Desktop",
    "Wifi Login Setup",
    "Extra Data",
    "credentials.json"
)
chromedriver_path = os.path.join(
    os.environ['USERPROFILE'],
    "Desktop",
    "Wifi Login Setup",
    "chromedriver"
)

# Load the JSON file
with open(json_path, "r") as file:
    credentials = json.load(file)

username = credentials["username"]
password = credentials["password"]

service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://secure.vcccd.edu/guest/student.php?cmd=login")
WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.ID, "ID_formdf673b6a_weblogin_user")))
driver.find_element(By.ID, "ID_formdf673b6a_weblogin_user").click()
driver.find_element(By.ID, "ID_formdf673b6a_weblogin_user").send_keys(username)
driver.find_element(By.ID, "ID_formdf673b6a_weblogin_password").click()
driver.find_element(By.ID, "ID_formdf673b6a_weblogin_password").send_keys(password)
driver.find_element(By.ID, "ID_formdf673b6a_weblogin_visitor_accept_terms").click()
driver.find_element(By.ID, "ID_formdf673b6a_weblogin_submit").click()

WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "here")))
print ("SUCESSFULLY CONNECTED TO INTERNET")
time.sleep(1)