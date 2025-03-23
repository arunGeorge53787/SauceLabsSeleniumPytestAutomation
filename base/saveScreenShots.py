import time
import os
from pathlib import Path

def saveScreenshot(driver, test_name):
    ssDir=Path('Screenshots')
    if not os.path.exists(ssDir):
        os.makedirs(ssDir)
    timestamp = time.strftime("%Y%m%d%H%M%S")
    ssName=f'{test_name}_{timestamp}.png'
    screenshot_path = f"{ssDir}/{ssName}"
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved: {screenshot_path}")
    return ssName
