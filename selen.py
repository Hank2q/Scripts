from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome(r'C:\Users\HASSANIN\Documents\chromedriver_win32\chromedriver.exe')
driver.get('https://www.reddit.com/r/MemeEconomy/')
page = driver.find_element_by_tag_name('html')

# TODO: pyautogui to click the block notification of chrome

for i in range(5):
    sleep(5)
    page.send_keys(Keys.END)
    