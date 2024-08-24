import urllib3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import json

urllib3.disable_warnings()

def json_get_url() -> list:
    with open('config.json', 'r') as rf:
        data = json.load(rf)
        rf.close()
        return data['url']

def driver_init():
    global driver
    driver = webdriver.Safari()
    driver.get(json_get_url())
    print('buben 1.0')
    while True:
        a = 5
        while a != 0:
            while True:
                try:
                    driver.find_element(By.XPATH, '//*[@id="clickButton"]').click()
                    break
                except Exception as e:
                    pass
            a = a - 1
            while True:
                try:
                    element = driver.find_element(By.ID, 'clickButton')
                    driver.execute_script("arguments[0].setAttribute('class', 'click-button')", element)
                    break
                except:
                    pass

driver_init()