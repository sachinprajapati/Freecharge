from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time


file = open("data.csv")
data = csv.reader(file)
# binary = FirefoxBinary('/usr/bin/firefox')
browser = webdriver.Firefox(executable_path='./geckodriver')

browser.get("https://www.freecharge.in/")
element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[1]/header/div/div[2]/span'))
    )
elem = browser.find_element_by_xpath('//*[@id="__next"]/div[1]/header/div/div[2]/span')
elem.click()

WebDriverWait(browser, 60).until((
    EC.url_to_be('https://www.freecharge.in/rentals/addLandlord')
))


for i in data:
    elem = browser.find_element_by_id('addLandlordName')
    elem.send_keys(Keys.CONTROL + "a")
    elem.send_keys(Keys.DELETE)
    elem.send_keys(i[2])

    elem = browser.find_element_by_id('addLandlordAccountNumber')
    elem.send_keys(Keys.CONTROL + "a")
    elem.send_keys(Keys.DELETE)
    elem.send_keys(i[0])

    elem = browser.find_element_by_id('addLandlordConfirmAccountNumber')
    elem.send_keys(Keys.CONTROL + "a")
    elem.send_keys(Keys.DELETE)
    elem.send_keys(i[0])

    elem = browser.find_element_by_id('addLandlordIfscCode')
    elem.send_keys(Keys.CONTROL + "a")
    elem.send_keys(Keys.DELETE)
    elem.send_keys(i[1])
    time.sleep(2)
    WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[5]/div[1]/div[1]/div/div[2]/div[3]/form/div[2]/button'))
    )
    elem = browser.find_element_by_xpath("/html/body/div[5]/div[1]/div[1]/div/div[2]/div[3]/form/div[2]/button")
    elem.click()
    WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div[1]/div[1]/div/div[2]/div[3]/form/div[2]/button'))
    )
    while True:
        if "Please try again" in browser.page_source:
            break
    time.sleep(1)


browser.quit()