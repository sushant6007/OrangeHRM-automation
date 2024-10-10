import pytest
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Configure logging for PyTest to display in the terminal
@pytest.fixture(scope="session", autouse=True)
def configure_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def login(driver, username="Admin", password="admin123"):
    try:
        logging.info(f"Test started: Logging in as user {username}")

        # Navigate to the login page
        driver.get("https://opensource-demo.orangehrmlive.com")

        # Enter username and password
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys(username)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "password"))).send_keys(password)

        # Click the login button
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]'))).click()

        # Wait for the 'Welcome' message
        welcome_message = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//p[normalize-space()='Time at Work']")))

        # Assert successful login
        assert welcome_message.is_displayed(), f"Login failed for user {username}"
        logging.info(f"Login successful for user {username}")

    except TimeoutException:
        logging.error("TimeoutException: Element loading timed out.")
        pytest.fail("Test failed due to timeout waiting for elements.")

    except NoSuchElementException as e:
        logging.error(f"Element not found - {e}")
        pytest.fail(f"Test failed due to missing element: {e}")

    except Exception as e:
        logging.error(f"Unexpected error occurred: {e}")
        pytest.fail(f"Test failed: {e}")



