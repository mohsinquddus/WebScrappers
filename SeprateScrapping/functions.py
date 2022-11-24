import pandas as pd
import numpy as np
import requests
import bs4
from bs4 import BeautifulSoup
import time
from selenium import webdriver
import pathlib
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import warnings

warnings.filterwarnings("ignore")


def get_Soup_from_requests(url):
    responce = requests.get(url)
    html = responce.text
    soup = BeautifulSoup(html, 'lxml')
    return soup


def get_soup_from_selenium(url):
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--headless')
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        driver = webdriver.Chrome("static/chromedriver.exe", options=options)
        driver.get(url)
        driver.maximize_window()
        time.sleep(2)
        scroll_pause_time = 1  # You can set your own pause time. My laptop is a bit slow so I use 1 sec
        screen_height = driver.execute_script("return window.screen.height;")  # get the screen height of the web
        i = 1
        while True:
            driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
            i += 1
            time.sleep(scroll_pause_time)
            scroll_height = driver.execute_script("return document.body.scrollHeight;")
            if (screen_height) * i > scroll_height:
                break
        #         driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        #         driver.implicitly_wait(20)
        page = driver.page_source
        soup = BeautifulSoup(page, "lxml")
        driver.close()
        driver.quit()
        return soup
    except Exception as e:
        print('Error Fetching data', e)


def get_soup_from_selenium_previous(url):
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        # options.add_argument('--headless')
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        #         driver = webdriver.Firefox(options=options)
        driver = webdriver.Chrome("static/chromedriver.exe", options=options)
        driver.get(url)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(7)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        # driver.maximize_window() # For maximizing window
        # driver.implicitly_wait(20)
        page = driver.page_source
        soup = BeautifulSoup(page, "lxml")
        driver.close()
        driver.quit()
        return soup
    except Exception as e:
        print('Error Fetching data', e)
