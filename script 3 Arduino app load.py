import subprocess
import pyautogui
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select

def main():
    # Specify the path to the Arduino IDE executable file
    arduino_path = r"C:\Program Files (x86)\Arduino\arduino.exe"
    
    # Specify the path to the file to be opened in the Arduino IDE
    file_path = r"C:\Users\orour\OneDrive\Documents\Arduino\messing\messing.ino"
    
    # Run the Arduino IDE executable file with the file path as an argument
    arduino_process = subprocess.Popen([arduino_path, file_path])
    
    # Wait for the IDE process to start up
    arduino_process.wait()
    
    # Wait for the IDE window to fully load
    time.sleep(12)
    
    # Use pyautogui to simulate keyboard and mouse actions to open the Tools menu and navigate to the Ports submenu
    pyautogui.hotkey('alt', 't')
    pyautogui.press('down', presses=4)  # Change the number of down arrow presses to navigate to the Ports submenu
    pyautogui.press('enter')
    
    # terminal is then open 
    time.sleep(2)
    #qwe are used in the arduino code to move the servo to certain angles
    pyautogui.typewrite('q')
    pyautogui.press('enter')
    print("The we have set the servo to its starting position")

    time.sleep(5)

    # Set the path to chrome in my file explorer
    chrome_driver_path = "C:\chromedriver.exe"

    # Create Chrome driver
    driver = webdriver.Chrome()

    # Navigate to the ESP32 cam webpage
    driver.get("http://172.20.10.2/")

    try:
        # Wait for the frame size dropdown to be available
        dropdown = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "framesize"))
        )

        # Select size of image 3 is the 240x240 (should be small and quicker may change size later ok for testing)
        Select(dropdown).select_by_value("3")

        # Wait for the button to be clickable and take photo
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "get-still"))
        )

        # Click the get still button
        element.click()

        #delay for the image to load up in the webpage before saving
        #this is prone to bugs if not quick enough look into this ************
        time.sleep(15)

        #save photo
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "save-still"))
        )

        # Click the take still button
        element.click()

        # Wait for the download to complete
        time.sleep(5)

         # Open Postman
        postman_path = r"C:\Users\orour\Downloads\Postman-win64-Setup.exe"
        os.startfile(postman_path)

        # Wait for Postman to open
        time.sleep(25)
       
       #this isnt the best way of doing this as it will only work on my pc look into this ***************
        # Click the Body button in Postman
        pyautogui.click(x=990, y=305)  # coordinates to match the position of the Body button 
        print("body button has been pressed")

        time.sleep(5)

        # Click the Select File button in Postman
        pyautogui.click(x=750, y=450)  # coordinates to match the position of the Select File button 
        print("select file button has been pressed")

        time.sleep(5)


    except TimeoutException:
        print("Error: Timed out waiting for element.")
    except:
        print("Error somewhere...")
    finally:
        # Keep the driver open while the window is open
        while True:
            if len(driver.window_handles) == 0:
                break


        # Quit the driver when the window is closed
        driver.quit()

if __name__ == "__main__":
    main()
