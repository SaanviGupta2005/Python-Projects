from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


chrome_driver_path = r"C:\Development\chromedriver.exe"
driver = webdriver.Chrome(service=Service(executable_path=chrome_driver_path))

# driver.get("https://www.amazon.com/dp/B08L3SW8DZ/ref=sbl_dpx_kitchen-electric-cookware_B08GC6PL3D_0?th=1")
# price = driver.find_element(by=By.CLASS_NAME, value="a-offscreen")
# print(price.text)

driver.get("https://www.python.org/")
event = driver.find_element(by=By.CSS_SELECTOR, value = ".menu li time")
print(event.text)
event_name = driver.find_element(by=By.CSS_SELECTOR, value = ".menu li a")
print(event_name.text)



driver.quit()
