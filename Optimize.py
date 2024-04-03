import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

with open("StepsByStep.xlsx", "r",  encoding="utf-8") as file:
    value = file.read()
url = value[1,2]
passWord = value[2,4]
ct = datetime.now()
ts = str(ct.timestamp())
email = value[1,4]

def openurl(webui):
    service_obj = Service("C:/Users/HP/OneDrive - PowerGate/Documents/chromedriver.exe")  # seleniumManager
    options = Options()
    options.add_experimental_option("detach", True)
    wDriver = webdriver.Chrome(options=options, service=service_obj)
    wDriver.get(webui)
    return wDriver

openurl(url)
print(value[1,2])

