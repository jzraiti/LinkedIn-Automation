from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import pyautogui as pag
import time
import os

def login_to_linkedin(driver):
    with open('secrets.txt', 'r') as file:
        lines = file.readlines()
        username_string = lines[0].strip()
        password_string = lines[1].strip()
        print(f"Username: {username_string}")
        print(f"Password: {password_string}")
    username = driver.find_element("name","session_key")
    username.send_keys(username_string)
    password = driver.find_element("name","session_password")
    password.send_keys(password_string)
    button = """//*[@id="main-content"]/section[1]/div/div/form/div[2]/button"""
    driver.find_element(By.XPATH,button).click()

def  start_bot(driver,url,network_url):
    driver.get(url)
    login_to_linkedin(driver)

def main():
    url =  "http://linkedin.com/"
    network_url =  "http://linkedin.com/mynetwork/"
    driver = webdriver.Chrome()
    start_bot(driver,url,network_url)


main()