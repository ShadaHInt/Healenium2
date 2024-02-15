from selenium import webdriver
from selenium.webdriver.common.by import By


# Set up ChromeDriver
driver = webdriver.Chrome()
driver = SelfHealingDriver(driver)  # Pass it to SelfHealingDriver

driver.maximize_window()
driver.get("https://www.google.co.in/")
driver.find_element(By.XPATH, "//a[text()='Gmail']").click()
driver.quit()
