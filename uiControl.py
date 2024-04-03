from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#--Chrome
service_obj = Service("C:/Users/HP/OneDrive - PowerGate/Documents/chromedriver.exe") # seleniumManager
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

#Checkbox list
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break

#radio button
radioButtons = driver.find_elements(By.CSS_SELECTOR, ".radioButton") #css selector .class
radioButtons[2].click()
assert radioButtons[2].is_selected()

#hide/show element
assert driver.find_element(By.CSS_SELECTOR, "#displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "show-textbox").click()
assert driver.find_element(By.CSS_SELECTOR, "#displayed-text").is_displayed()
