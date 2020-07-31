from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from concurrent.futures import ThreadPoolExecutor
import shelve


def check_yop(mail):
    browser = webdriver.Chrome()
    browser.get('http://www.yopmail.com/en/')
    browser.implicitly_wait(5)
    login = browser.find_element_by_css_selector('#login')
    login.send_keys(mail)
    login.send_keys(Keys.ENTER)


data = shelve.open('cash/test_mails')
mails = data['mails']
data.close()

with ThreadPoolExecutor() as exe:
    exe.map(check_yop, mails)



