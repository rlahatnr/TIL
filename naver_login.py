from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyperclip as pc
import random

def login(driver, uid, pwd):
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-popup-blocking")
    driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2F')
    driver.implicitly_wait(10)
    time.sleep(1)

    id_box = driver.find_element_by_id('id')
    pw_box = driver.find_element_by_id('pw')

    pc.copy(uid)
    id_box.send_keys(Keys.CONTROL, 'v')
    time.sleep(random.random() + 1)
    pc.copy(pwd)
    pw_box.send_keys(Keys.CONTROL, 'v')
    pw_box.send_keys(Keys.RETURN)
    time.sleep(random.random() + 1)

def iframe(driver, frame_name):
    for iframe in driver.find_elements_by_css_selector('iframe'):
        if iframe.get_attribute('name') == frame_name:
            driver.switch_to.frame(frame_name)
            time.sleep(1)
        else:
            driver.refresh()
            time.sleep(1)