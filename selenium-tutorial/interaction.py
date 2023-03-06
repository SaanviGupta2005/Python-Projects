from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys


chrome_driver_path = r"C:\Development\chromedriver.exe"
driver = webdriver.Chrome(service=Service(executable_path=chrome_driver_path))

# driver.get("https://en.wikipedia.org/wiki/Wikipedia:Contents")
# count = driver.find_element(by=By.CSS_SELECTOR, value="#articlecount a")
# print(count.text)

# all_portals = driver.find_element(by=By.LINK_TEXT, value="Portals")
# all_portals.click()

# search = driver.find_element(by=By.NAME, value="search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)


# driver.get("http://secure-retreat-92358.herokuapp.com/")
#
# search = driver.find_element(by=By.NAME, value="fName")
# search.send_keys("Saanvi")
#
# search = driver.find_element(by=By.NAME, value="lName")
# search.send_keys("Gupta")
#
# search = driver.find_element(by=By.NAME, value="email")
# search.send_keys("pythonabcdefgh@gmail.com")
#
# submit = driver.find_element(by=By.CSS_SELECTOR, value="form button")
# submit.click()


driver.get("https://orteil.dashnet.org/cookieclicker/")
submit = driver.find_element(by= By.ID, value= "cookieAnchor")
submit.click()
