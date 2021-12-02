# Import Webdriver
from selenium import webdriver

# Chrome Driver
driver = webdriver.Chrome(
    executable_path="E:/Programming Hero/Projects/rokomari-selenium-test/rokomari-python-selenium/chromedriver.exe"
)

# Home Page Test
driver.get("https://www.rokomari.com/book")
