import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

url = "http://practice.automationtesting.in/"
passWord = 'Autotest@123'
ct = datetime.now()
ts = str(ct.timestamp())
email = "thom" + ts + "@yopmail.com"


def openurl(webui):
    service_obj = Service("C:/Users/HP/OneDrive - PowerGate/Documents/chromedriver.exe")  # seleniumManager
    options = Options()
    options.add_experimental_option("detach", True)
    wDriver = webdriver.Chrome(options=options, service=service_obj)
    wDriver.get(webui)
    return wDriver


# -----Case 1: Registration
# tion-Sign-in---------
driver = openurl(url)
time.sleep(3)
driver.find_element(By.XPATH, "//a[@href='https://practice.automationtesting.in/my-account/']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//form[@class='register']/p[1]/input").send_keys(email)
driver.find_element(By.XPATH, "//form[@class='register']/p[2]/input").send_keys(passWord)
wait = WebDriverWait(driver, 15)
wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//input[@value='Register']")))
time.sleep(2)
driver.find_element(By.XPATH, "//input[@value='Register']").click()
time.sleep(2)
with open('accounts.txt', 'w') as writer:
    writer.writelines("{},{}\n".format(email, passWord))
    writer.close()
assert driver.find_element(By.XPATH, "//a[text()='Logout']").is_displayed()

driver.quit()
print("Case 1: Registered successfully")

# -----------Case login-----------
driver = openurl(url)
time.sleep(10)
driver.find_element(By.XPATH, "//a[@href='https://practice.automationtesting.in/my-account/']").click()
time.sleep(3)

with open('accounts.txt', 'r') as file:
    contents = file.read().split(",")

driver.find_element(By.XPATH, "//input[@name='username'][@id='username']").send_keys(contents[0])
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div[1]/div/div[1]/form/p[2]/input").send_keys(contents[1])
# wait = WebDriverWait(driver, 15)
# wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//input[@name='login'][@value='Login']")))
# time.sleep(3)
#driver.find_element(By.XPATH, "//input[@name='login']").click()
time.sleep(2)
assert driver.find_element(By.XPATH, "//a[text()='Logout']").is_displayed()
driver.quit()
print("-----login success-------")
# -----------Case 2: Registration with invalid Email-id-----------
time.sleep(3)
driver = openurl(url)
time.sleep(3)
driver.find_element(By.XPATH, "//a[@href='https://practice.automationtesting.in/my-account/']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//form[@class='register']/p[1]/input").send_keys("email@gmail")
driver.find_element(By.XPATH, "//form[@class='register']/p[2]/input").send_keys(passWord)
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

# -----------Case 3: Registration with empty Email-id-----------
driver = openurl(url)
time.sleep(3)
driver.find_element(By.XPATH, "//a[@href='https://practice.automationtesting.in/my-account/']").click()
driver.find_element(By.XPATH, "//form[@class='register']/p[1]/input").send_keys("")

el = driver.find_element(By.XPATH, "//form[@class='register']/p[2]/input")
for character in passWord:
    el.send_keys(character)
    time.sleep(1)
# driver.find_element(By.XPATH,"//form[@class='register']/p[2]/input").send_keys("Autotest@123")

time.sleep(3)
wait = WebDriverWait(driver, 30)
wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//input[@value='Register']")))
driver.find_element(By.XPATH, "//input[@value='Register']").click()
time.sleep(3)
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located(
    (By.XPATH, "//li[text()=' Please provide a valid email address.']")))
assert driver.find_element(By.XPATH, "//li[text()=' Please provide a valid email address.']").is_displayed()
driver.quit()
print("Case 3: Register failed with empty Email-id")

# -----------Case 4: Registration with empty password-----------
driver = openurl(url)
driver.find_element(By.XPATH, "//a[@href='https://practice.automationtesting.in/my-account/']").click()
driver.find_element(By.XPATH, "//form[@class='register']/p[1]/input").send_keys("thom999@yopmail.com")
driver.find_element(By.XPATH, "//form[@class='register']/p[2]/input").send_keys("")
time.sleep(5)
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//input[@value='Register']")))
driver.find_element(By.XPATH, "//input[@value='Register']").click()
time.sleep(5)
assert driver.find_element(By.XPATH, "//li[text()=' Please enter an account password.']").is_displayed()
driver.quit()
print("Case 4: Register failed with empty password")

# -----------Case 5: Registration with empty Email-id & password-----------
driver = openurl(url)
driver.find_element(By.XPATH, "//a[@href='https://practice.automationtesting.in/my-account/']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//input[@value='Register']").click()
time.sleep(3)
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//li[text()=' Please provide a valid email address.']")))
assert driver.find_element(By.XPATH, "//li[text()=' Please provide a valid email address.']").is_displayed()
driver.quit()
print("Case 5: Register failed with empty email & password")
