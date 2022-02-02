import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://www.saucedemo.com/")
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(3)
prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
price_list = []
for price in prices:
    strip_price = float(price.text.replace("$", ""))
    price_list.append(strip_price)
price_list.sort(reverse=True)
for i in range(1, 7):
    check_item = driver.find_element(By.XPATH, "(//*[@class='inventory_item_price'])["+str(i)+"]")
    if str(price_list[0]) in check_item.text:
        driver.find_element(By.XPATH, "(//*[@class='pricebar']/button)["+str(i)+"]").click()
        break
time.sleep(1)
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
time.sleep(1)
cart_price = driver.find_element(By.CLASS_NAME,"inventory_item_price").text.replace("$","")
assert float(cart_price) == price_list[0]





