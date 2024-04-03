import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
#--Chrome
service_obj = Service("C:/Users/HP/OneDrive - PowerGate/Documents/chromedriver.exe") # seleniumManager
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=service_obj)

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2) # 2 second
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(countries))

for country in countries:
    if country.text == "India":
        country.click()
        break

# get text từ dynamic dropdown
#print(driver.find_element(By.ID, "autosuggest").text) - text dynamic k lấy dc bằng .text, phải dùng get_attribute("value")
assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"
print(driver.find_element(By.ID, "autosuggest").get_attribute("value"))

