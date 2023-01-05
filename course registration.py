from selenium import webdriver
import time


driver = webdriver.Chrome(r"./chromedriver.exe")

driver.get("https://colleague-ss.uoguelph.ca/Student/Planning/DegreePlans")

driver.maximize_window()
time.sleep(20)

while True:
    button = driver.find_element_by_id("register-button")
    button.click()
    time.sleep(10)