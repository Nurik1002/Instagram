from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.service import Service  
from webdriver_manager.chrome import ChromeDriverManager
import time

def login_to_instagram(username, password):


    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  
    service = Service(ChromeDriverManager().install())

    driver = None

    try:
        driver = webdriver.Chrome(service=service, options=options)
        driver.get("https://www.instagram.com/accounts/login/")

        
        driver.implicitly_wait(5)

        
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        username_field.send_keys(username)

        
        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        password_field.send_keys(password)

     
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        )
        login_button.click()

        
        time.sleep(5)
        print(driver.current_url)
    
        if "accounts/login" in driver.current_url:
            print(f"Login failed: Invalid username or password passwd : {password}")
            
        else:
            print(f"\n=====================\nLogin successful!\nuname: {username}\npasswd : {password}\n=====================\n")

    except TimeoutException as e:
        print(f"Login failed: Timeout ({e})")
    except NoSuchElementException as e:
        print(f"Login failed: Element not found ({e})")
    finally:
        if driver:
            driver.quit()






username = "one.1nsta"
password = "XxXnurikinsta"

login_to_instagram(username, password)
