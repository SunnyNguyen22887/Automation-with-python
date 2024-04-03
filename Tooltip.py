from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("C:/Users/HP/OneDrive - PowerGate/Documents/chromedriver.exe")  # seleniumManager
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=service_obj)

driver.get("https://practice.automationtesting.in/my-account/")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.XPATH, "//form[@class='register']/p[1]/input").send_keys("ab")
driver.find_element(By.XPATH, "//form[@class='register']/p[2]/input").send_keys("Autotest@123")
wait = WebDriverWait(driver, 15)
wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//input[@value='Register']")))
driver.find_element(By.XPATH, "//input[@value='Register']").click()
toolTip = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//form[@class='register']/p[1]/input")))
hov = ActionChains(driver).move_to_element(toolTip)
txt = hov.perform()
tooltipText = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='tippy-content']"))).text
print(tooltipText)