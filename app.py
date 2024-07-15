from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException, WebDriverException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import logging
import time

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def login_to_instagram(username, password):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  
    service = Service(ChromeDriverManager().install())
    driver = None

    try:
        driver = webdriver.Chrome(service=service, options=options)
        driver.get("https://www.instagram.com/accounts/login/")

        wait = WebDriverWait(driver, 10, poll_frequency=0.5)

        # Input username and password
        for locator, keys in [
            (By.CSS_SELECTOR, 'input[name="username"]', username),
            (By.CSS_SELECTOR, 'input[name="password"]', password)
        ]:
            element = wait.until(
                EC.presence_of_element_located(locator)  
            )
            element.clear()
            element.send_keys(keys)

        # Click login button
        wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        ).click()

        # Check for successful login
        try:
            wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'div._aarf'))
            )
            logging.info(f"\n=====================\nLogin successful!\nuname: {username}\npasswd : {password}\n=====================\n")
        except TimeoutException:
            logging.error("Login failed: Unable to find profile name after login.")

    except WebDriverException as e:
        logging.error(f"WebDriverException: {e}")
        
    except (TimeoutException, NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException) as e:
        logging.error(f"Login failed due to element issues: {e}")
        
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        
    finally:
        if driver is not None:
            driver.quit()

username = input("Enter your Instagram username: ")
password = input("Enter your Instagram password: ")

login_to_instagram(username, password)