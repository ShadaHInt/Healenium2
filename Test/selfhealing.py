from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up a WebDriver instance (you should configure the WebDriver as needed)
driver = webdriver.Chrome()

try:
    # Navigate to the login page
    driver.get('file:///C:/Users/shadan/Downloads/applightwebsite/Applight/index.html')  # Replace with the actual login page URL
    element = driver.find_element(By.XPATH,'//*[@id="navbarSupportedContent"]/ul/li[7]/a')
    element.click()
    # Define the attribute and value to identify the input field (you can adjust this based on your needs)
    input_field_attribute = 'name'
    input_field_value = 'full-name'

    # Wait for the input field to be visible and interactable
    input_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, f'input[{input_field_attribute}="{input_field_value}"]'))
    )

    # Example usage:
    # You can directly interact with the input field without needing modified HTML
    input_field.send_keys("your_email@example.com")  # Replace with your email

    # Continue with any other interactions or actions on the page

finally:
    # Quit the WebDriver when done
    driver.quit()
