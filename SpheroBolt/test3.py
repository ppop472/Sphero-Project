import time
from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI
import keyboard
import threading
import json

print('Running.')

def spin_robot(api, robot_id):
    with api:
        time.sleep(1)
        api.spin(360, 1)
        time.sleep(1)
        api.set_heading(0)
        time.sleep(1)
        while True:
            try:
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
                elif keyboard.is_pressed('b'):
                    api.spin(360, 1)
                elif keyboard.is_pressed('q'):
                    break  
                elif keyboard.is_pressed('r'):
                    print(f"Reconnecting to Robot {robot_id}...")
                    api.reconnect()
                else:
                    api.roll(0, 0, 0)

                time.sleep(0.1)

            except Exception as e:
                print(f"Error occurred: {e}")
                print(f"Connection error with Robot {robot_id}: {e}")
                print(f"Reconnecting to Robot {robot_id}...")
                api.reconnect()

def load_robots_from_config():
    with open('robots_config.json', 'r') as config_file:
        config = json.load(config_file)
        return [(SpheroEduAPI(toy), robot['id_keyword']) for toy in scanner.find_toys() for robot in config['robots'] if any(keyword in str(toy) for keyword in [robot['id_keyword']])]

robots = load_robots_from_config()
threads = []

for i, (robot, robot_id) in enumerate(robots):
    print(f'Robot{i + 1} (ID: {robot_id}) movement')
    thread = threading.Thread(target=spin_robot, args=(robot, robot_id))
    threads.append(thread)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print('End')
