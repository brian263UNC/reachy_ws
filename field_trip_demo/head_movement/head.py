from reachy_sdk import ReachySDK
import time

class Head:
    def __init__(self):
        self.reachy = ReachySDK(host='10.42.0.1') #TODO be sure to change the IP address appropriately
        self.accepted_commands = ["happy", "sad", "look_a", "look_d", "look_u"]

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
        #TODO
        pass

    def look_down(self):
        #TODO
        pass

    def look_up(self):
        #TODO
        pass

    def run(self, action):
        print(action)
        if action not in self.accepted_commands or len(action) < 3:
            print("Command Not Found")
        elif action == "happy":
            self.happy_antennas()

        elif action == "sad":
            self.sad_antennas()

        elif action == "look_a":
            self.look_around()

        elif action == "look_d":
            self.look_down()

        elif action == "look_u":
            self.look_up()



def main(args):
    head_movement = Head()
    head_movement.run(args)

if __name__ == "__main__":
    while True:
        action = input("Head Movement?: happy, sad, look_a, look_d,look_u")
        main(action)
