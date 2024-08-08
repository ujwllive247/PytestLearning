import time

import pytest
from selenium import webdriver


@pytest.mark.smoke
def test_Google_com():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://www.google.com/")
    time.sleep(3)
    driver.quit()



def test_facebook_come():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://www.facebook.com/")
    time.sleep(3)
    driver.quit()

@pytest.mark.smoke
def test_omayo_come():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("http://omayo.blogspot.com/")
    time.sleep(3)
    driver.quit()


def test_herokoo_com():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/")
    time.sleep(3)
    driver.quit()
