# Original Sourcecode from https://github.com/Mizan-Ali/Zoom_Automation/blob/master/Zoom.py

from datetime import datetime

import keyboard
import pandas as pd
import pyautogui
import subprocess

# reading the meeting details
df = pd.read_csv('timetable.csv')
df_new = pd.DataFrame()

while (True):
    # Check the current system time
    time = datetime.now().strftime("%H:%M")
    # Check if the current time is mentioned in the Dataframe
    if time in df.Time.values:
        df_new = df[df['Time'].astype(str).str.contains(time)]
        # Open the Zoom app(Insert the Zoom Path on your Devide below)
        subprocess.Popen("/Applications/zoom.us.app")
        time.sleep(15)
        # Locate the position of the join button on the screen
        position = pyautogui.locateOnScreen("buttons\\join_button.png")
        # Move the cursor to the position of the button
        pyautogui.moveTo(position)
        # Perform click operation
        pyautogui.click()
        time.sleep(2)
        # Write the meeting ID from the dataframe onto the Zoom App
        keyboard.write(df_new.iloc[0, 1])

        # For tapping the Turn off video option on Zoom app
        position = pyautogui.locateOnScreen("buttons\\turn_off_vid_button.png")
        pyautogui.moveTo(position)
        pyautogui.click()
        time.sleep(2)

        # For tapping on the Join button
        position = pyautogui.locateOnScreen("buttons\\join_button_2.png")
        pyautogui.moveTo(position)
        pyautogui.click()
        time.sleep(7)

        # Reads the Meeting Passcode from the dataframe and enters into the zoom app
        keyboard.write(str(int(df_new.iloc[0, 2])))
        time.sleep(3)

        # For finally joining the meeting
        position = pyautogui.locateOnScreen("buttons\\join_meeting.png")
        pyautogui.moveTo(position)
        pyautogui.click()

        # Wait for one minute before the next iteration starts
        time.sleep(60)
