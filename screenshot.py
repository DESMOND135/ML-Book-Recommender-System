from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Start browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open your Streamlit app
driver.get("http://localhost:8501")

# Wait for the app to load
time.sleep(5)

# Scroll to bottom slowly (to force load all elements)
scroll_pause_time = 1
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(scroll_pause_time)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Now set window size to full height
driver.set_window_size(1920, last_height)

# Save full screenshot
driver.save_screenshot("app_full_screenshot.png")

driver.quit()

print("✅ Full screenshot saved as app_full_screenshot.png")
