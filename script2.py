from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select


def main():
    # Set the path to chrome in my file explorer
    chrome_driver_path = "C:\chromedriver.exe"

    # Create Chrome driver
    driver = webdriver.Chrome()

    # Navigate to the ESP32 cam webpage
    driver.get("http://172.20.10.2/")

    # Select the dropdown to change size of image
    dropdown = Select(driver.find_element_by_id("framesize"))

    # Select size of image 3 is the 240x240 (should be small and quicker may change size later ok for testing)
    dropdown.select_by_value("3")

    try:
        # Wait for the element to be clickable
        element = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.ID, "get-still"))
        )

        # Click the button
        element.click()

        #error check buttons
    except TimeoutException:
        print("Error: Button not clicked within 1 minute.")
    except:
        print("Error clicking button.")
    finally:
        # Keep the driver open while the window is open
        while True:
            if len(driver.window_handles) == 0:
                break

        # Quit the driver when the window is closed
        driver.quit()

if __name__ == "__main__":
    main()
