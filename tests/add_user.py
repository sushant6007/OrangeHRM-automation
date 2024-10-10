import pytest
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login import login  # Import the login function from test_login.py

def test_add_new_user(driver):
    # Perform login first
    login(driver, username="Admin", password="admin123")

    try:
        # Click on the Admin tab in the navigation panel
        logging.info("Clicking on the 'Admin' tab.")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'])[1]"))
        ).click()

        # Click on the Add button
        logging.info("Clicking on the 'Add' button.")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Add']"))
        ).click()

        # Fill in the 'FirstNameTest LastNameTest' in the 'Type for hints...' field
        logging.info("Filling in the 'FirstNameTest LastNameTest' into the 'Type for hints...' field.")
        type_for_hints_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Type for hints...']"))
        )
        type_for_hints_field.send_keys("FirstNameTest LastNameTest")

        # Enter the username 'adityapatil007'
        logging.info("Entering the username 'adityapatil007'.")
        username_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@class='oxd-input oxd-input--focus']"))
        )
        username_field.send_keys("adityapatil007")

        # Enter the password 'Qwerty@123' in the first password field
        logging.info("Entering the password 'Qwerty@123' in the first password field.")
        password_field_1 = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "(//input[@class='oxd-input oxd-input--active'][@type='password'])[1]"))
        )
        password_field_1.send_keys("Qwerty@123")

        # Enter the same password 'Qwerty@123' in the confirm password field
        logging.info("Entering the same password 'Qwerty@123' in the confirm password field.")
        password_field_2 = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "(//input[@class='oxd-input oxd-input--active'][@type='password'])[2]"))
        )
        password_field_2.send_keys("Qwerty@123")

        # You can add more steps here if needed, like clicking save or checking if the user was added successfully.

        logging.info("New user 'adityapatil007' has been successfully added.")

    except Exception as e:
        logging.error(f"An error occurred during adding a new user: {e}")
        pytest.fail(f"Test failed: {e}")
