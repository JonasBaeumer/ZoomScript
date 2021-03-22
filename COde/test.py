import datetime
from datetime import time
from turtle import pd

import pyautogui
import subprocess

subprocess.Popen("/Applications/OBS.app")
position = pyautogui.locateOnScreen("buttons\\recording_button.png")
# Move the cursor to the position of the button
pyautogui.moveTo(position)
# Perform click operation
pyautogui.click()
time.sleep(2)

df = pd.read_csv('timetable.csv')
while True:
    time = datetime.now().strftime("%H:%M")
    if time not in df.Time.values:
        position = pyautogui.locateOnScreen("button\\stoprecording_button.png")
        pyautogui.moveTo(position)
        break


