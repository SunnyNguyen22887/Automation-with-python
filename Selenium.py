from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#--Chrome
# service_obj = Service("C:/Users/HP/OneDrive - PowerGate/Documents/chromedriver.exe") # seleniumManager
# driver = webdriver.Chrome(service=service_obj)

#--firefox
# service_obj = Service("C:/Users/HP/OneDrive - PowerGate/Documents/geckodriver.exe")
# driver = webdriver.Firefox(service=service_obj)

#--edge
service_obj = Service("C:/Users/HP/OneDrive - PowerGate/Documents/msedgedriver.exe") # seleniumManager
driver = webdriver.Edge(service=service_obj)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com")
print(driver.title)
print(driver.current_url)

driver.get("https://rahulshettyacademy.com/practice-project")

driver.minimize_window()
driver.back() #back trên trình duyệt
driver.refresh()
driver.forward() # nút next trình duyệt

driver.close()
