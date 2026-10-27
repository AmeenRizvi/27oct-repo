from datetime import datetime
from playsound import playsound
import time

alarm = input("Enter alarm time (HH:MM): ")

while True:
    if datetime.now().strftime("%H:%M") == alarm:
        print("⏰ Alarm ringing!")
        playsound("alarm.mp3")
        break
    time.sleep(1)
