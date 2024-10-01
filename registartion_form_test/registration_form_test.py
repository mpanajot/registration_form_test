from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import unittest

class TestJoinNow(unittest.TestCase):

    def setUp(self):
        # Initialize the WebDriver
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)  # Wait for elements to be ready

    def test_join_now(self):
        driver = self.driver
        # step1: Navigate to the URL
        driver.get('https://moneygaming.qa.gameaccount.com/')

        # step2: Wait for the JOIN NOW button to be clickable and click it
        join_now_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.newUser.green'))
        )
        join_now_button.click()

        # step3: Select a title value from the dropdown
        driver.find_element(By.ID, 'title').click()
        driver.find_element(By.CSS_SELECTOR, '#title option[value="Mr"]').click()

        # step4: Enter first name and surname
        first_name_field = driver.find_element(By.ID, 'forename')
        first_name_field.send_keys('Martin')
        surname_field = driver.find_element(By.NAME, 'map(lastName)')
        surname_field.send_keys('Panajotov')

        # step5: Check the tickbox
        driver.find_element(By.NAME, 'map(terms)').click()

        # step6: Submit the form
        driver.find_element(By.ID, 'form').click()

        # step7: Validate the validation message
        try:
            validation_message = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, '.error[for="dob"]'))
            )
            validation_text = validation_message.text
            self.assertEqual(validation_text, 'This field is required')
        except TimeoutException:
            self.fail("Validation message not displayed.")

    def tearDown(self):
        # Close the browser
        self.driver.quit()

# Run the test
if __name__ == '__main__':
    unittest.main()
