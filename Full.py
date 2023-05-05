import os
import time
import subprocess
import pyautogui
import json
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

#open the arduino application
def open_arduino(arduino_path, file_path):
    arduino_process = subprocess.Popen([arduino_path, file_path])
    arduino_process.wait()

    # Wait for the IDE window to fully load
    time.sleep(20)  

#set the top servo so the tablet is in the view of the camera
def setTopServo():
    # Use pyautogui to simulate keyboard and mouse actions to open the Tools menu and navigate to the Ports submenu
    pyautogui.hotkey('alt', 't')
    pyautogui.press('down', presses=4)  # Change the number of down arrow presses to navigate to the Ports submenu
    pyautogui.press('enter')
    
    # terminal is then open 
    time.sleep(2)

    #Serial monitor is used in the arduino code to move the servo to certain angles
    #r in this case moves the op servo to the starting location
    pyautogui.typewrite('t')
    pyautogui.press('enter')
    print("The we have set the servo to its starting position")

    #close the serial monitor and the application 
    time.sleep(2)
    pyautogui.hotkey('alt', 'f4')
    time.sleep(.2)
    pyautogui.hotkey('alt', 'f4')

    time.sleep(1)

#navigate to the local host. Take and save an image
def take_photo():
    try:
        chrome_driver_path = "C:\chromedriver.exe"
        driver = webdriver.Chrome(chrome_driver_path)
        driver.get("http://172.20.10.2/")
        dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "framesize")))
        Select(dropdown).select_by_value("3")
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "get-still")))
        element.click()
        time.sleep(10)
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "save-still")))
        element.click()
        time.sleep(5)
    except:
        print("Error taking photo")


#open postman application 
def open_postman():
    try:
         # Open Postman
        postman_path = r"C:\Users\orour\Downloads\Postman-win64-Setup.exe"
        os.startfile(postman_path)

        # Wait for Postman to open
        time.sleep(40)
    except:
        print("Error opening Postman")

#navigate postman and enter the photo to find its tag
def send_photo():
    try:
        #body button press
        pyautogui.click(x=990, y=305)
        time.sleep(1)
        #delete previous image
        pyautogui.click(x=825, y=430)
        time.sleep(1)
        #add new  image
        pyautogui.click(x=680, y=420)
        time.sleep(1)
        pyautogui.hotkey('alt', 'd')
        time.sleep(1)
        pyautogui.typewrite(r"C:\Users\orour\Downloads")
        pyautogui.press('enter')
        time.sleep(2)
        for i in range(4):
            pyautogui.press('tab')
            time.sleep(.2)
        pyautogui.hotkey('space')
        pyautogui.hotkey('enter')
        print("Photo has been selected")
        time.sleep(2)
        pyautogui.click(x=1750, y=270)
        time.sleep(6)
    except:
        print("Error sending photo")

#place output recieved form postman and find out the highest probability
def edit_file():
    pyautogui.click(x=990, y=705)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(.1)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(.5)
    file_path = r"C:\Users\orour\Scripts\probability.txt"
    os.startfile(file_path)

    time.sleep(3)

    # Paste the copied content into the file
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(.1)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(.1)
    pyautogui.hotkey('ctrl', 's')
    time.sleep(.5)

    # Read the modified file content into a Python object
    with open(file_path, 'r') as p:
        data = p.read()

    # Parse the JSON data into a Python object
    data_dict = json.loads(data)

    # Find the prediction with the highest probability and print its tagName
    max_prediction = max(data_dict['predictions'], key=lambda x: x['probability'])
    tag_name = max_prediction['tagName']
    print(tag_name)

    time.sleep(5)  

    # Perform the appropriate action based on the tag_name value
    if tag_name == 'Blue':
        arduino_path = r"C:\Program Files (x86)\Arduino\arduino.exe"
        file_path = r"C:\Users\orour\OneDrive\Documents\Arduino\3_servos\3_servos.ino"
        open_arduino(arduino_path, file_path)
        
        # Wait for the IDE window to fully load
        time.sleep(15)  
        # Use pyautogui to simulate keyboard and mouse actions to open the Tools menu and navigate to the Ports submenu
        pyautogui.hotkey('alt', 't')
        pyautogui.press('down', presses=4)  # Change the number of down arrow presses to navigate to the Ports submenu
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.typewrite('w')
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.typewrite('r')
        pyautogui.press('enter')
        #close the serial monitor and the application 
        time.sleep(2)

            #Serial monitor is used in the arduino code to move the servo to certain angles
        #r in this case moves the op servo to the starting location
        pyautogui.typewrite('t')
        pyautogui.press('enter')
        print("The we have set the servo to its starting position")
        time.sleep(2)

        pyautogui.hotkey('alt', 'f4')
        time.sleep(.2)
        pyautogui.hotkey('alt', 'f4')


    elif tag_name == 'BigWhite':
        arduino_path = r"C:\Program Files (x86)\Arduino\arduino.exe"
        file_path = r"C:\Users\orour\OneDrive\Documents\Arduino\3_servos\3_servos.ino"
        open_arduino(arduino_path, file_path)
        # Wait for the IDE window to fully load
        time.sleep(15)  
        # Use pyautogui to simulate keyboard and mouse actions to open the Tools menu and navigate to the Ports submenu
        pyautogui.hotkey('alt', 't')
        pyautogui.press('down', presses=4)  # Change the number of down arrow presses to navigate to the Ports submenu
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.typewrite('e')
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.typewrite('r')
        pyautogui.press('enter')
        #close the serial monitor and the application 
        time.sleep(2)

            #Serial monitor is used in the arduino code to move the servo to certain angles
        #r in this case moves the op servo to the starting location
        pyautogui.typewrite('t')
        pyautogui.press('enter')
        print("The we have set the servo to its starting position")
        time.sleep(2)

        pyautogui.hotkey('alt', 'f4')
        time.sleep(.2)
        pyautogui.hotkey('alt', 'f4')
        


    elif tag_name == 'Mix':
        arduino_path = r"C:\Program Files (x86)\Arduino\arduino.exe"
        file_path = r"C:\Users\orour\OneDrive\Documents\Arduino\3_servos\3_servos.ino"
        open_arduino(arduino_path, file_path)
        # Wait for the IDE window to fully load
        time.sleep(15)  
        # Use pyautogui to simulate keyboard and mouse actions to open the Tools menu and navigate to the Ports submenu
        pyautogui.hotkey('alt', 't')
        pyautogui.press('down', presses=4)  # Change the number of down arrow presses to navigate to the Ports submenu
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.typewrite('q')
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.typewrite('r')
        pyautogui.press('enter')
        #close the serial monitor and the application 
        time.sleep(2)

        #Serial monitor is used in the arduino code to move the servo to certain angles
        #r in this case moves the op servo to the starting location
        pyautogui.typewrite('t')
        pyautogui.press('enter')
        print("The we have set the servo to its starting position")

        time.sleep(2)
        pyautogui.hotkey('alt', 'f4')
        time.sleep(.2)
        pyautogui.hotkey('alt', 'f4')

    #if its an unkown tag the sorter is empty so the script ends
    else:
        print("Unknown tag name: " + tag_name)
        sys.exit()

#loop main so the script keeps running in a 
def main():
    #arduino_path = r"C:\Program Files (x86)\Arduino\arduino.exe"
    #file_path = r"C:\Users\orour\OneDrive\Documents\Arduino\3_servos\3_servos.ino"
    #open_arduino(arduino_path, file_path)
    #setTopServo()
    take_photo()
    open_postman()
    send_photo()
    edit_file()

if __name__ == "__main__":
    while True:
        main()