from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#--Chrome
service_obj = Service("C:/Users/HP/OneDrive - PowerGate/Documents/chromedriver.exe") # seleniumManager
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=service_obj)
driver.get("https://pinnacleqm.com/")
driver.find_element(By.XPATH, "//span[@class='elementor-button-text']").click()
