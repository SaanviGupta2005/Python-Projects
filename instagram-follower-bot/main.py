import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException


chrome_driver_path = "C:\Development\chromedriver.exe"
similar_account = "pycoders"
username = "cute_smiley_06"
password = "abcd1234()"


class InstaFollower:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(service=Service(executable_path=driver_path))

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)
        email_login = self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input')
        email_login.send_keys(username)
        password_login = self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_login.send_keys(password)
        time.sleep(2)
        password_login.send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{similar_account}")

        time.sleep(5)
        followers = self.driver.find_element(by=By.XPATH,
                                             value='/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/ul/li[2]/a/div/span')
        followers.click()

        time.sleep(5)
        modal = self.driver.find_elements(by=By.XPATH,
                                          value='/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        while True:
            follows = self.driver.find_elements(by=By.XPATH,
                                                value='/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/div[3]/button')
            for button in follows:
                try:
                    button.click()
                    time.sleep(1)
                except ElementClickInterceptedException:
                    cancel_button = self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
                    cancel_button.click()


bot = InstaFollower(chrome_driver_path)
bot.login()
bot.find_followers()
bot.follow()
