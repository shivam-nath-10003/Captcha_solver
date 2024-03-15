# CAPTCHA Solver and Downloader

This Python script automates the process of solving CAPTCHAs, submitting them, and triggering downloads from a website. It utilizes image processing and OCR (Optical Character Recognition) techniques to extract text from CAPTCHA images and interact with UI elements.

## Dependencies
- Python 3.9
- pyautogui
- Pillow
- pytesseract

## Usage
1. Clone or download the repository.
2. Install dependencies using the above command.
3. Run the script `captcha_solver_downloader.py`.
4. Ensure that the CAPTCHA images and UI elements have consistent positions on the screen.
5. Adjust the hardcoded screen coordinates and timing delays if necessary.
6. Execute the script and observe the automated CAPTCHA solving and download triggering process.

## Functionality
- The script automatically clicks on the activation button, reads the CAPTCHA text, enters it into the input box, submits the form, and triggers the download.
- It includes handling for restricted areas and scrolling down the page after each iteration.
- CAPTCHA text extraction is performed using Tesseract OCR.
- Screenshots are captured using Pillow library, and mouse actions are simulated using pyautogui.




