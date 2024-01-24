import time
from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI
from spherov2.types import Color
import keyboard
import threading

print('Running.')

def spin_robot(api):
    with api:
        api.spin(360, 1)
        api.set_heading(0)
        
        while True:
            if keyboard.is_pressed('w'):
                api.set_heading(0)
                api.set_speed(100)
            elif keyboard.is_pressed('s'):
                api.set_heading(180)
                api.set_speed(100)
            elif keyboard.is_pressed('a'):
                api.set_heading(270)
                api.set_speed(100)
            elif keyboard.is_pressed('d'):
                api.set_heading(90)
                api.set_speed(100)
            elif keyboard.is_pressed('q'):
                break  # exit the loop if 'q' is pressed
            else:
                api.roll(0, 0, 0)  # stop the robot if no key is pressed

            time.sleep(0.1)

toys = scanner.find_toys()
robot1 = None
robot2 = None

for toy in toys:
    toy_name = str(toy)
    if 'CB1E' in toy_name:
        robot1 = SpheroEduAPI(toy)
    elif '4FCE' in toy_name:
        robot2 = SpheroEduAPI(toy)

threads = []

if robot1:
    print('Robot1 movement')
    thread1 = threading.Thread(target=spin_robot, args=(robot1,))
    threads.append(thread1)

if robot2:
    print('Robot2 movement')
    thread2 = threading.Thread(target=spin_robot, args=(robot2,))
    threads.append(thread2)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print('End')
