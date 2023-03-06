from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(service=Service(chrome_driver_path))

driver.get(
    "https://www.linkedin.com/jobs/search/?currentJobId=3280343659&f_AL=true&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&refresh=true")
time.sleep(5)

sign_in_button = driver.find_element(by=By.LINK_TEXT, value="Sign in")
sign_in_button.click()

email_login = driver.find_element(by=By.ID, value="username")
email_login.send_keys("pythonabcdefgh@gmail.com")

password_login = driver.find_element(by=By.ID, value="password")
password_login.send_keys("abcd1234()")
password_login.send_keys(Keys.ENTER)

time.sleep(5)
apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-apply-button")
apply_button.click()

time.sleep(4)
phone_button = driver.find_element(by=By.CLASS_NAME, value=".fb-single-line-text")

if phone_button == "":
    phone_button.send_keys("1234567890")

submit_button = driver.find_element(by=By.ID, value="#ember370")
submit_button.click()
