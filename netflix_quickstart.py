from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
from urllib.parse import quote_plus

# Get movie title from user input
movie_title = input("Enter the movie name to search: ")
encoded_title = quote_plus(movie_title)

chrome_options = Options()
#Replace YOUR_USERNAME in both files, commit, and push!
chrome_options.add_argument(
    "--user-data-dir=/Users/YOUR_USERNAME/selenium-profile")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--remote-debugging-port=9222")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")

# Launch browser with your profile
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.netflix.com")

# Wait for page to load
time.sleep(5)

# Profile selection (if prompted)
try:
    driver.find_element(By.XPATH, "//span[text()='Sravya']").click()
    time.sleep(5)
except:
    print("No profile prompt, continuing...")

# Search for the user-provided movie
search_url = f"https://www.netflix.com/search?q={encoded_title}"
driver.get(search_url)
print(f"Searching for '{movie_title}'...")
time.sleep(5)

# Click the first movie result
try:
    driver.find_element(By.XPATH, "//a[contains(@href, '/watch/')]").click()
    print("Movie clicked.")
except:
    print("Could not click the movie. Please check the title or try manually.")
    input("Press Enter to close...")
    driver.quit()
    exit()

# Play/Resume the movie
try:
    time.sleep(3)
    driver.find_element(
        By.XPATH,
        "//button[.//span[contains(text(),'Resume')] or .//span[contains(text(),'Play')]]"
    ).click()
    print("Play/Resume clicked.")
except:
    print("Play/Resume button not found.")

# Enter fullscreen
try:
    time.sleep(5)
    ActionChains(driver).move_by_offset(200, 200).perform()
    time.sleep(2)
    driver.find_element(
        By.XPATH,
        "//button[contains(@aria-label,'Full screen') or contains(@aria-label,'Enter full screen')]"
    ).click()
    print("Fullscreen clicked.")
except Exception as e:
    print("Fullscreen failed:", e)

# Keep browser open until user decides to close
input("Press Enter to close the browser...")
driver.quit()
