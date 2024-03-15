import time
import pyautogui
from PIL import Image
from pytesseract import image_to_string

# Function to read text from an image using Tesseract OCR
def read_text_from_image(region):
    screenshot = pyautogui.screenshot(region=region)
    text = image_to_string(screenshot)
    return text.strip()

# Function to solve captcha, submit, and trigger download
def process_captcha_and_download():
    # Set your own cursor positions based on your screen resolution
    activation_click_position = (222, 833)
    captcha_box_coordinates = [(732, 225), (843, 225), (843, 268), (732, 268)]
    captcha_entry_position = (472, 249)
    submit_button_position = (945, 346)
    download_button_position = (499, 294)
    activation_center_position = (222, 833)  # Update this with the actual position
    restricted_area = [(150, 444), (150, 1796), (2694, 444), (2694, 1796)]

    # Step 0: Initial wait for 3 seconds
    time.sleep(5)

    # Loop for 5 times
    for _ in range(100000):
        # Step 1: Move to the activation click position and click
        activation_center = pyautogui.locateCenterOnScreen('/Users/shivamnath/Desktop/IIMV internship/capctcha breaker/s1.jpg', confidence=0.9)
        if (restricted_area[0][1]<activation_center[1]):
            activation_center_half = (activation_center[0] // 2, activation_center[1] // 2)
            a = (activation_center_half[0]+50, activation_center_half[1] - 40)
            pyautogui.moveTo(a)
        #time.sleep(2)
            pyautogui.click()
            time.sleep(1)
        else:
            print('iteration skipped')
            pyautogui.scroll(-3)
            continue
        # Step 2: Read captcha text from the screen
        captcha_text = read_text_from_image((captcha_box_coordinates[0][0], captcha_box_coordinates[0][1],
                                             captcha_box_coordinates[1][0] - captcha_box_coordinates[0][0],
                                             captcha_box_coordinates[3][1] - captcha_box_coordinates[0][1]))

        print(f"Detected Captcha: {captcha_text}")

        # Step 3: Enter captcha into the box
        pyautogui.moveTo(captcha_entry_position)
        pyautogui.click()
        pyautogui.typewrite(captcha_text)
        time.sleep(1)

        # Step 4: Click the submit button
        pyautogui.moveTo(submit_button_position)
        pyautogui.click()
        time.sleep(1)

        # Step 5: Click the download button
        pyautogui.moveTo(download_button_position)
        pyautogui.click()
        time.sleep(1)

        # Step 6: Move the cursor back to position 'a'
        pyautogui.moveTo(a)
        time.sleep(1)

        # Step 7: Perform downward scrolling
        pyautogui.scroll(-3)
        pyautogui.click()
        pyautogui.scroll(-4)
        time.sleep(2)

# Example usage
process_captcha_and_download()
