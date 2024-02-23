from reachy_sdk import ReachySDK
import time

class Head:
    def __init__(self):
        self.reachy = ReachySDK(host='10.42.0.1') #TODO be sure to change the IP address appropriately
        self.accepted_commands = ["happy", "sad", "look_a", "look_d", "look_u"]

    def head_lock(self):
        self.reachy.turn_on('head')

    def head_unlock(self):
        self.reachy.turn_off('head')

    def happy_antennas(self):
        self.reachy.head.l_antenna.speed_limit = 0.0
        self.reachy.head.r_antenna.speed_limit = 0.0
    
        for _ in range(9):
            self.reachy.head.l_antenna.goal_position = 10.0
            self.reachy.head.r_antenna.goal_position = -10.0
            time.sleep(0.1)

            self.reachy.head.l_antenna.goal_position = -10.0
            self.reachy.head.r_antenna.goal_position = 10.0
            time.sleep(0.1)
        self.reachy.head.l_antenna.goal_position = 0.0
        self.reachy.head.r_antenna.goal_position = 0.0

    def sad_antennas(self):
        self.reachy.head.l_antenna.speed_limit = 70.0
        self.reachy.head.r_antenna.speed_limit = 70.0
        
        self.reachy.head.l_antenna.goal_position = 140.0
        self.reachy.head.r_antenna.goal_position = -140.0
        time.sleep(5.0)
        
        self.reachy.head.l_antenna.goal_position = 0.0
        self.reachy.head.r_antenna.goal_position = 0.0

    def look_around(self):
        self.reachy.head.look_at(x=0.5, y=-0.5, z=0.1, duration=1.0)
        time.sleep(0.1)

        self.reachy.head.look_at(x=0.5, y=0, z=-0.4, duration=1.0)
        time.sleep(0.1)

        self.reachy.head.look_at(x=0.5, y=0.3, z=-0.3, duration=1.0)
        time.sleep(0.1)

        self.reachy.head.look_at(x=0.5, y=0, z=0, duration=1.0)

    def look_down(self):
        self.reachy.head.look_at(x=0.5, y=0, z=-0.4, duration=1.0)
        time.sleep(0.1)

        self.reachy.head.look_at(x=0.5, y=0, z=0, duration=1.0)

    def look_up(self):
        self.reachy.head.look_at(x=0.5, y=0, z=0.4, duration=1.0)
        time.sleep(0.1)

        self.reachy.head.look_at(x=0.5, y=0, z=0, duration=1.0)

    def run(self, action):
        print(action)
        if action not in self.accepted_commands or len(action) < 3:
            print("Command Not Found")

        elif action == "happy":
            self.head_lock()
            self.happy_antennas()
            self.head_unlock()

        elif action == "sad":
            self.head_lock()
            self.sad_antennas()
            self.head_unlock()

        elif action == "look_a":
            self.head_lock()
            self.look_around()
            self.head_unlock()

        elif action == "look_d":
            self.head_lock()
            self.look_down()
            self.head_unlock()

        elif action == "look_u":
            self.head_lock()
            self.look_up()
            self.head_unlock()

def main(args):
    head_movement = Head()
    head_movement.run(args)

if __name__ == "__main__":
    while True:
        action = input("Which movement?: happy, sad, look_a, look_d,look_u")
        if action == "q":
            break
        main(action)
    SystemExit