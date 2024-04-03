from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/Users/HP/OneDrive - PowerGate/Documents/chromedriver.exe")  # seleniumManager
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

#----------hover-------------
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform() #right mouse click
# action.drag_and_drop()
action.move_to_element(driver.find_element(By.LINK_TEXT, "Top")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()
driver.quit()
#---------open new tab-------------

