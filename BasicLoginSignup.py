import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from bs4 import BeautifulSoup

url = "http://practice.automationtesting.in/"

service_obj = Service("C:/Users/HP/OneDrive - PowerGate/Documents/chromedriver.exe")  # seleniumManager
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=service_obj)

#-----Case 1: Registration-Sign-in---------
driver.get(url)
ct = datetime.now()
ts = str(ct.timestamp())
email = "thom"+ts+"@yopmail.com"
# remove ad
# Get the HTML source of the page
html = driver.page_source
# Parse the HTML using Beautiful Soup
soup = BeautifulSoup(html, "html.parser")
# Remove the elements containing ads
for ad in soup.select(".ad"):
  ad.decompose()
# Save the modified HTML
modified_html = str(soup)
# Overwrite the HTML of the web page with the modified HTML
driver.execute_script(f"document.documentElement.innerHTML = {modified_html!r}")
time.sleep(3)
driver.find_element(By.XPATH, "//a[@href='https://practice.automationtesting.in/my-account/']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//form[@class='register']/p[1]/input").send_keys(email)
driver.find_element(By.XPATH,"//form[@class='register']/p[2]/input").send_keys("Autotest@123")
wait = WebDriverWait(driver, 15)
wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//input[@value='Register']")))
time.sleep(2)
driver.find_element(By.XPATH, "//input[@value='Register']").click()
time.sleep(2)
assert driver.find_element(By.XPATH, "//a[text()='Logout']").is_displayed()
driver.quit()
print("Case 1: Registered successfully")
#-----------Case 2: Registration with invalid Email-id-----------
service_obj = Service("C:/Users/HP/OneDrive - PowerGate/Documents/chromedriver.exe")  # seleniumManager
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=service_obj)
driver.get(url)
time.sleep(3)
driver.find_element(By.XPATH, "//a[@href='https://practice.automationtesting.in/my-account/']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//form[@class='register']/p[1]/input").send_keys("email@gmail")
driver.find_element(By.XPATH,"//form[@class='register']/p[2]/input").send_keys("Autotest@123")
wait = WebDriverWait(driver, 20)
wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//input[@value='Register']")))
time.sleep(3)
driver.find_element(By.XPATH, "//input[@value='Register']").click()
time.sleep(3)
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//li[text()=' Please provide a valid email address.']")))
assert driver.find_element(By.XPATH, "//li[text()=' Please provide a valid email address.']").is_displayed()
driver.quit()
print("Case 2: Register failed with invalid Email-id")

#-----------Case 3: Registration with empty Email-id-----------
service_obj = Service("C:/Users/HP/OneDrive - PowerGate/Documents/chromedriver.exe")  # seleniumManager
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=service_obj)
driver.get(url)
time.sleep(3)
driver.find_element(By.XPATH, "//a[@href='https://practice.automationtesting.in/my-account/']").click()
driver.find_element(By.XPATH,"//form[@class='register']/p[1]/input").send_keys("")
driver.find_element(By.XPATH,"//form[@class='register']/p[2]/input").send_keys("Autotest@123")
time.sleep(3)
wait = WebDriverWait(driver, 90)
wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//input[@value='Register']")))
driver.find_element(By.XPATH, "//input[@value='Register']").click()
time.sleep(3)
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//li[text()=' Please provide a valid email address.']")))
assert driver.find_element(By.XPATH, "//li[text()=' Please provide a valid email address.']").is_displayed()
driver.quit()
print("Case 3: Register failed with empty Email-id")

#-----------Case 4: Registration with empty password-----------
service_obj = Service("C:/Users/HP/OneDrive - PowerGate/Documents/chromedriver.exe")  # seleniumManager
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=service_obj)
driver.get(url)
driver.find_element(By.XPATH, "//a[@href='https://practice.automationtesting.in/my-account/']").click()
driver.find_element(By.XPATH,"//form[@class='register']/p[1]/input").send_keys("thom99@yopmail.com")
driver.find_element(By.XPATH,"//form[@class='register']/p[2]/input").send_keys("")
time.sleep(5)
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//input[@value='Register']")))
driver.find_element(By.XPATH, "//input[@value='Register']").click()
time.sleep(5)
assert driver.find_element(By.XPATH, "//li[text()=' Please enter an account password.']").is_displayed()
driver.quit()
print("Case 4: Register failed with empty password")

#-----------Case 5: Registration with empty Email-id & password-----------
service_obj = Service("C:/Users/HP/OneDrive - PowerGate/Documents/chromedriver.exe")  # seleniumManager
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=service_obj)
driver.get(url)
driver.find_element(By.XPATH, "//a[@href='https://practice.automationtesting.in/my-account/']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//input[@value='Register']").click()
time.sleep(3)
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//li[text()=' Please provide a valid email address.']")))
assert driver.find_element(By.XPATH, "//li[text()=' Please provide a valid email address.']").is_displayed()
driver.quit()
print("Case 5: Register failed with empty email & password")
