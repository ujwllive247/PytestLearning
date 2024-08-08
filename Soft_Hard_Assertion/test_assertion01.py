
from selenium import  webdriver
from selenium.webdriver.common.by import By


def test_tutorials_ninja():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")

    expected_title = "Your Store" # This is correct title.
    expected_title = "Your Store123"  # This is incorrect title.
    actual_title = driver.title
    assert actual_title.__eq__(expected_title)  # Hard Assertion ::  We don't want to stop code because of this assertion.
    # Main purpose is verify the second assertion.
    driver.find_element(By.NAME,"search").send_keys("HP")
    driver.find_element(By.XPATH,"//button[contains(@class,'btn-default')]").click()
    assert driver.find_element(By.LINK_TEXT,"HP LP3065").is_displayed()
    driver.quit()


    # for soft assertion , we need to install labrary   pip install pytest-soft-assertions

    # To run the test ........ pytest --soft-asserts