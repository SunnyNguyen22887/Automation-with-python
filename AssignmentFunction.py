import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#--Chrome
service_obj = Service("C:/Users/HP/OneDrive - PowerGate/Documents/chromedriver.exe") # seleniumManager
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=service_obj)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

#assignment function:
expectedList = ['Cucumber - 1 Kg','Raspberry - 1/4 Kg','Strawberry - 1/4 Kg']
actualList =[]
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(3)

results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
print(len(results))
count = len(results)
assert count == 3
#cart and checkout
for result in results:
    actualList.append(result.find_element(By.XPATH,"h4").text)
    result.find_element(By.XPATH, "div/button").click()  # click cả 3 button

assert expectedList == actualList
print(actualList)

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
time.sleep(4)

#sum validation
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum = 0
for price in prices:
    sum = sum + int(price.text)

print(sum)
totalAmount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)

assert sum == totalAmount

time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

#explicit wait
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
promo = driver.find_element(By.CSS_SELECTOR, ".promoInfo").text
print(promo)
assert promo == "Code applied ..!"

# assert total amount and total disacount amount
discountedAmount = float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)

assert totalAmount > discountedAmount








