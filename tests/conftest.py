import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Set up the Chrome WebDriver path
@pytest.fixture(scope="module")
def driver():
    service = Service('C:\\Users\\susha\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()
