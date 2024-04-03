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

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.implicitly_wait(5000)
driver.find_element(By.NAME,"email").send_keys("thom@yopmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID,"exampleCheck1").click()
driver.implicitly_wait(5000)

# xpath - //tagname[@attribute='value'] -> //input[@type='submit']
# css - tagname[@attribute='value'] -> input[@type='submit'], #id
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Rahul")
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
#(//input[@type='text'])[3]

#static sropdown
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
#dropdown.select_by_index(1)
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)
#dropdown.select_by_value()




driver.find_element(By.XPATH,"//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "success" in message  #verify success text display on message

driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("hello")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()


