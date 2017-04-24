#!/home/bohr/Development/python/news/bin/python3
# -*- coding: utf-8 -*-

'''
Created on 01 Jan 2017

@author: deus
'''
#===============================================================================
# Standard Modules
#===============================================================================
import datetime



#===============================================================================
# 3rd Party Modules
#===============================================================================
import config
from lxml import etree
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

parser = etree.HTMLParser(remove_comments=True,encoding='utf8')
namespace = dict(re='http://exslt.org/regular-expressions')

def wait_click(driver, wait, xpath):

    try:
        element = WebDriverWait(driver, wait).until(EC.presence_of_element_located((By.XPATH, xpath)))
        #print('Found clickable element...')
        click(driver, xpath)
    except:
        print('Failed on xpath ' + xpath)
        driver.quit()

    return

def wait_post(driver, wait, xpath, keys):

    try:
        element = WebDriverWait(driver, wait).until(EC.presence_of_element_located((By.XPATH, xpath)))
        #print('Found postable element...')
        post(driver, xpath, keys)
    except:
        driver.quit()

    return

def click(driver, xpath):

    elem = driver.find_element_by_xpath(xpath)
    elem.click()
    #print('Clicked on element...')

    return

def post(driver, xpath, keys):

    elem = driver.find_element_by_xpath(xpath)
    elem.click()
    elem.clear()
    elem.send_keys(keys)
    #print('Posted to element...')

    return

def get_handles(driver):

    handles = []
    for handle in driver.window_handles:
        handles.append(handle)

    return handles

def do_login(driver):

    driver.get('http://www.racingpost.com/horses2/results/home.sd')
    driver.find_element_by_xpath('//a[@id="signInLink"]').click()
    iframes = driver.find_elements_by_tag_name('iframe')
    for i in range(0, len(iframes)):
        driver.switch_to_frame(iframes[i])
        login = re.match('https://reg.racingpost.com/mpp/sign_in.sd', driver.current_url)
        if login:
            elem = driver.find_element_by_xpath('//input[@type="email"]')
            elem.click()
            elem.send_keys(config.USER)
            elem = driver.find_element_by_xpath('//input[@type="password"]')
            elem.click()
            elem.send_keys(config.PASS)
            elem = driver.find_element_by_xpath('//button')
            elem.click()
        driver.switch_to_default_content()

    return

def init_driver():

    # Configure and instantiate Chromium
    options = webdriver.ChromeOptions()
    options.add_argument('/home/bohr/.config/chromium/Default')
    options.add_argument('--disable-infobars')
    driver = webdriver.Chrome('/home/bohr/Development/python/dissertation/chromedriver')

    return driver

def main():

#------------------------------------------------------------------------------
    began = datetime.datetime.now().time().strftime("%H:%M:%S")
    print('Started at: ====> ' + began)
#------------------------------------------------------------------------------
	#===========================================================================
    # Comment
    #===========================================================================
    init_driver()
    do_login(driver)







#------------------------------------------------------------------------------
    completed = datetime.datetime.now().time().strftime("%H:%M:%S")
    print('Finished at: ====> ' + completed)
#------------------------------------------------------------------------------
    return


if __name__ == '__main__':
    main()
