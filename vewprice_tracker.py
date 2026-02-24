from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


def prices ():
    driver.get("https://www.google.com/")
    driver.maximize_window()
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("google")
    search_box.send_keys(Keys.RETURN)

prices()


