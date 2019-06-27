## directions:
# 1. snap inbox to left half of screen using magnets
# 2. set inbox to show unread first and have box unchecked

import pyautogui
import time

time.sleep(3)
screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()
pyautogui.moveTo(200, 190)
pyautogui.click() # make chrome the focus

# main loop
for x in range(180):
    pyautogui.moveTo(280, 190) # move to "select"
    pyautogui.click()
    time.sleep(1.5)
    pyautogui.moveTo(490, 190) # move to "mark as read"
    pyautogui.click()
    time.sleep(1.5)
    pyautogui.moveTo(280, 190) # move to "select"
    pyautogui.click()
    time.sleep(1.5)
    pyautogui.moveTo(340, 190) # move to "refresh"
    pyautogui.click()
    time.sleep(1.5)
