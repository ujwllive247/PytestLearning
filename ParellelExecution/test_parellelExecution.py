import time

from selenium import webdriver


def test_omayo():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://omayo.blogspot.com")
    time.sleep(5)
    driver.quit()


def test_tutorialninjaz():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    time.sleep(5)
    driver.quit()


def test_Facebook():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://facebook.com")
    time.sleep(5)
    driver.quit()

    #  https://the-internet.herokuapp.com/


def test_internetheroku():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/")
    time.sleep(5)
    driver.quit()


def test_Flipkart():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://flipkart.com")
    time.sleep(5)
    driver.quit()



def test_Amazon():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://Amazon.com")
    time.sleep(5)
    driver.quit()



