import time
from time import sleep

from pycparser.ply.yacc import format_stack_entry
from selenium import webdriver
from selenium.webdriver.common.by import By

#Variable declaration
wait = 5
url = "https://www.saucedemo.com/"
username = "standard_user"
password = "secret_sauce"
firstname = "Uti"
lastname =  "Ike"
postalcode =  "223045"

#Browser initialization
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

#Login Details
UserName =driver.find_element(By.ID, "user-name")
UserName.send_keys("standard_user")

PassWord =driver.find_element(By.ID, "password")
Password.send_keys("secret_sauce")

Login = driver.find_element(By.ID, "login-button")
Login.click()
time.sleep(wait)

#Add to Cart
Backpack =driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
Backpack.click()

BikeLight =driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
BikeLight.click()

Tshirt =driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
Tshirt.click()

onesie =driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
onesie.click()

Redshirt =driver.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")
Redshirt.click()

Jacket =driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket")
Jacket.click()

Cart_container =driver.find_element(By.ID, "shopping_cart_container")
Cart_container.click()

#Checkout details
driver.find_element(By.ID, "first-name").send_keys("Uti")
driver.find_element(By.ID, "last-name").send_keys("Ike")
driver.find_element(By.ID, "postal-code").send_keys("223045")
driver.find_element(By.ID, "continue").click()
driver.find_element(By.ID, "finish").click()
driver.find_element(By.ID, "back-to-products").click()
time.sleep(wait)


