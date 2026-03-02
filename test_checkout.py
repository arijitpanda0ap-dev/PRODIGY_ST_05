from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

# Step 1: Open Website
driver.get("https://www.saucedemo.com/")

# Step 2: Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

assert "inventory" in driver.current_url
driver.save_screenshot("screenshots/inventory.png")
print("Login Successful")

# Step 3: Add Item to Cart
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

assert "cart" in driver.current_url
driver.save_screenshot("screenshots/cart.png")
print("Item added to cart")

# Step 4: Checkout
driver.find_element(By.ID, "checkout").click()

driver.find_element(By.ID, "first-name").send_keys("John")
driver.find_element(By.ID, "last-name").send_keys("Doe")
driver.find_element(By.ID, "postal-code").send_keys("700001")
driver.find_element(By.ID, "continue").click()

assert "checkout-step-two" in driver.current_url
driver.save_screenshot("screenshots/checkout_form.png")
print("Checkout Step One Completed")

# Step 5: Finish Order
driver.find_element(By.ID, "finish").click()

success_message = driver.find_element(By.CLASS_NAME, "complete-header").text
assert "Thank you for your order!" in success_message
driver.save_screenshot("screenshots/order_success.png")
print("Order Completed Successfully")

time.sleep(3)
driver.quit()