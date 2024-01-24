import time
from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI
from spherov2.types import Color
import keyboard

toys = scanner.find_toys()
toy_t = []
for toy in toys:
    if 'CB1E' in str(toys):
        toy_t.append(toy)

if toy_t:
    with SpheroEduAPI(toy_t[0]) as api:
        speed = 0
        heading = 0

        while True:
                
            if keyboard.is_pressed('w'):
                speed = min(speed + 10, 100)
                api.set_heading(0)
                api.set_speed(speed)

            elif keyboard.is_pressed('s'):
                speed = min(speed + 10, 100)
                api.set_heading(180)
                api.set_speed(speed)

            elif keyboard.is_pressed('d'):
                speed = min(speed + 10, 100)
                api.set_heading(90)
                api.set_speed(speed)

            elif keyboard.is_pressed('a'):
                speed = min(speed + 10, 100)
                api.set_heading(270)
                api.set_speed(speed)

            elif keyboard.is_pressed('b'):
                api.spin(360, 1)

            else:
                speed = 0
                api.set_speed(speed)

            time.sleep(0.01)  
else:
    print("No Sphero toys found.")
    