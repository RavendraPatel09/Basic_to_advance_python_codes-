from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/login")
element = driver.find_element(By.XPATH, "/html/body/div[2]/nav/div/a[2]") 
element.click()
# print(element)
time.sleep(5)
element= driver.find_element(By.XPATH,'//*[@id="first-name"]')
element.send_keys("sam@gmail.com")
driver.quit()
