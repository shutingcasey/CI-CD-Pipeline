from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from webdriver_manager.chrome import ChromeDriverManager

# Install compatible ChromeDriver automatically
service = Service(ChromeDriverManager().install())

# Set Chrome options for headless mode (required for GitHub Actions)
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Initialize WebDriver
driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get("https://students.senecapolytechnic.ca/")
    print("✅ Successfully opened the student portal")

    link = driver.find_element(By.LINK_TEXT, "Academic")
    link.click()
    print("✅ Successfully clicked Academic")
    time.sleep(5)

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[@title='Accessible Learning Services']"))
    )
    element.click()
    print("✅ Successfully clicked Accessible Learning Services")
    time.sleep(5)

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Who We Are"))
    )
    element.click()
    print("✅ Successfully clicked Who We Are")
    time.sleep(5)

    driver.back()
    driver.back()
    driver.back()
    time.sleep(5)
    driver.forward()
    time.sleep(5)

except Exception as e:
    print(f"❌ Test failed: {e}")

finally:
    driver.quit()
    print("Test completed, browser closed")
