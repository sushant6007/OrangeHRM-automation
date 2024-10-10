import pytest
import logging
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login import login  # Import the login function

def test_search_admin_user(driver):
    # Perform login first
    login(driver, username="Admin", password="admin123")

    try:
        # Click on the Admin tab in the navigation panel
        logging.info("Clicking on the 'Admin' tab.")
        time.sleep(7)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'])[1]"))
        ).click()

        # Wait for the search field in the admin panel
        logging.info("Waiting for the Admin search panel.")
        search_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]"))
        )

        # Enter admin username to search
        logging.info("Searching for the admin username 'Admin'.")
        search_input.send_keys("Admin")

        # Click the search button
        logging.info("Clicking the search button.")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        ).click()

        # Wait for the search results to appear and verify the admin user
        logging.info("Verifying the search results.")
        result_user = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='oxd-table-card']//div[2]//div[1][contains(text( ), 'Admin')]"))
        )

        # Assert that the admin username 'Admin' is present in the results
        assert result_user.text == "Admin", "Admin user not found in the search results."
        logging.info("Admin user found in the search results.")

    except Exception as e:
        logging.error(f"An error occurred during admin search: {e}")
        pytest.fail(f"Test failed: {e}")
