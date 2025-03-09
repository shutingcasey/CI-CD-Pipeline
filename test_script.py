from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set Chrome options for headless mode (no GUI in GitHub Actions)
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Initialize WebDriver
driver = webdriver.Chrome(options=options)

try:
    # Open Seneca student portal
    driver.get("https://students.senecapolytechnic.ca/")
    print(" Successfully opened the student portal")

    # Click on the "Academic" link
    link = driver.find_element(By.LINK_TEXT, "Academic")
    link.click()
    print("Successfully clicked Academic")
    time.sleep(5)

    # Wait for and click "Accessible Learning Services"
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[@title='Accessible Learning Services']"))
    )
    element.click()
    print("Successfully clicked Accessible Learning Services")
    time.sleep(5)

    # Wait for and click "Who We Are"
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Who We Are"))
    )
    element.click()
    print("Successfully clicked Who We Are")
    time.sleep(5)

    # Use back and forward navigation
    driver.back()
    print("Successfully navigated back")
    time.sleep(2)
    driver.back()
    print("Successfully navigated back to Academic")
    time.sleep(2)
    driver.back()
    print("Successfully navigated back to Home")
    time.sleep(2)
    driver.forward()
    print("Successfully navigated forward")
    time.sleep(2)

except Exception as e:
    print(f"Test failed: {e}")

finally:
    # Ensure WebDriver is closed properly
    driver.quit()
    print("Test completed, browser closed")
