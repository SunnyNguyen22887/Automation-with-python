import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#--Chrome
service_obj = Service("C:/Users/HP/OneDrive - PowerGate/Documents/chromedriver.exe") # seleniumManager
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=service_obj)

urlroot = 'https://tinhte.vn/forums/xe-hoi.545/'
driver.get(urlroot)
time.sleep(2)
Dict ={"tieu de" : [], "noi dung" : []}
titles = (driver.find_elements(By.XPATH, "//ol/li/div[2]/div/h3/a[2]"))
# urls = driver.find_elements(By.XPATH, "//ol/li/div[2]/div/h3/a[2]")
total = 0
listURL = []
for title in titles:
    Dict["tieu de"].append(title.text)
    listURL.append(title.get_attribute('href'))
    total = total + 1
    if total >= 10:
        break

for url in listURL:
    total1 = 0
    driver.get(url)
    content_element = driver.find_element(By.CLASS_NAME, "xf-body-paragraph")
    content = content_element.text.strip()
    content = ' '.join(content.split())
    Dict["noi dung"].append(content)
    total1 = total1 + 1
    if total1 >= 10:
        break

# print(Dict)
driver.quit()
dataframe = pd.DataFrame(Dict)
dataframe.to_excel('example.xlsx', header=False, index=False)


