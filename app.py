from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import pyautogui as pag
import time
import os

def login_to_linkedin(driver):
    with open(os.path.dirname(__file__) + r'\secrets.txt', 'r') as file:
        lines = file.readlines()
        username_string = lines[0].strip()
        password_string = lines[1].strip()
    username = driver.find_element("name","session_key")
    username.send_keys(username_string)
    password = driver.find_element("name","session_password")
    password.send_keys(password_string)
    button = """//*[@id="main-content"]/section[1]/div/div/form/div[2]/button"""
    driver.find_element(By.XPATH,button).click()

def  goto_network_page(driver,network_url):
  driver.get(network_url)

def scroll_down(driver):
    """A method for scrolling the page."""
    # Get scroll height.
    last_height = driver.execute_script("return document.body.scrollHeight")
    for i in range(0,3):
        # Scroll down to the bottom.
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load the page.
        time.sleep(2)
        # Calculate new scroll height and compare with last scroll height.
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def send_requests_to_users(driver):
    time.sleep(5) # Sleep for 15 seconds - make sure window loads all the way
    all_buttons = driver.find_elements(By.TAG_NAME,"button")
    all_connect_buttons = []
    for button in all_buttons:
        if button.accessible_name == r"Invite {:member} to connect":
            print("Found button")
            all_connect_buttons.append(button)
            #pag.click(441, 666)
    for connect_button in all_connect_buttons:
        print("Clicking button")
        connect_button.click()
    print("Done !")

def zoom_out(n):
    pag.keyDown('ctrl')
    j: int = 1
    for j in range(n):
        pag.press('-')
        time.sleep(1)
    pag.keyUp('ctrl')

def  take_a_screenshot(driver):
    loc_time = time.localtime()
    loc_time = time.strftime("%Y-%m-%d_%H-%M-%S", loc_time)
    cwd = os.path.dirname(__file__) + r"/screenshots/" + loc_time + r".png"
    ss = driver.get_screenshot_as_png()
    try:
        os.makedirs(cwd, exist_ok=True)
        with open(cwd, "wb") as ss_file: # changes to how the file is opened
            ss_file.write(ss)
            print(f"Screenshot saved at {cwd}")
    except Exception as err:
        print(f"Screenshot save failed with {type(err).__name__}: {err}")
    print("Screenshot taken")


if __name__ == "__main__":
    url =  "http://linkedin.com/"
    network_url =  "http://linkedin.com/mynetwork/"
    driver = webdriver.Chrome()

    driver.get(url)
    login_to_linkedin(driver)
    goto_network_page(driver,network_url)
    zoom_out(6)
    send_requests_to_users(driver)
    take_a_screenshot(driver)
    driver.quit()