import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from robot.libraries.Screenshot import Screenshot
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def open_browser_nvidia(browser):
    if str(browser).lower() == "chrome":
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Edge()
    driver.maximize_window()

    return driver


def launch_site(driver, site):
    print(driver, site)
    driver.get(site)
    driver.implicitly_wait(2)


def click_product_tab(driver, product_locator):
    print("Click on Product tab")
    wait_till_till_element_exist(driver, product_locator)
    driver.find_element(By.XPATH, product_locator).click()
    time.sleep(2)


def select_laptop_from_product_tab(driver, laptop_button_locator):
    print("Click on laptop button")
    wait_till_till_element_exist(driver, laptop_button_locator)
    driver.find_element(By.XPATH, laptop_button_locator).click()



def taking_screenshot():
    obj = Screenshot()
    obj.take_screenshot()


def click_solution_tab(driver, solution_locator):
    print("Click on laptop button")
    wait_till_till_element_exist(driver, solution_locator)
    driver.find_element(By.XPATH, solution_locator).click()


def select_cloud_from_solution_tab(driver, cloud_locator):
    print("Click on laptop button")
    wait_till_till_element_exist(driver, cloud_locator)
    driver.find_element(By.XPATH, cloud_locator).click()

def wait_till_till_element_exist(driver, element):
    try:
        WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.XPATH, element)))
    except Exception as e:
        print("element not found due to: ", e)




