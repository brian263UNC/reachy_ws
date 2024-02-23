from mobile_base_sdk import MobileBaseSDK

class Entrance_Movement:
    def __init__(self):
        self.mobile_base = MobileBaseSDK('10.42.0.1') # Make sure to update the IP address yours TODO
        self.arrived_at_goal = False # boolean check if Reachy has arrived at the set goal
        self.final_distance = 4.0 # distance to travel in meters
        self.right_turn = 90
        self.left_turn = -90
        self.x = 0
        self.y = 0
        self.step_increase = 0.5

    def reset_coordinates(self):
        self.mobile_base.reset_odometry()

    def accelerate(self):
        # TODO
        pass

    def total_distance_traveled(self, x, y, theta):
        # TODO
        pass

    # Reset's the coordinate system and then spins Reachy by the desired degree amount
    def spin(self, degree):
        self.reset_coordinates()
        self.mobile_base.goto(x=0.0, y=0.0, theta=degree)

    def update_pos(self, x, y, step):
        return [x + step, y + step]

    def run(self):
        travel_distance = 0.0
        while(True):
            total_revolutions = 6
            for _ in range(total_revolutions):
                print("Current X: " + self.x, "Current Y: " + self.y)    
                new_pos = self.update_pos(self.x, self.y, self. step_increase) #iteration steps might be a bit too much
                self.mobile_base.goto(x=new_pos[0], y=new_pos[1], theta=0)
                print("New X: " + new_pos[0], "New Y: " + new_pos[1])
            self.reset_coordinates()
            travel_distance += 3.0
            print("Total distance traveled: " + travel_distance)
            if travel_distance >= self.final_distance: break # real ugly, but gets the job done, if the distance traveled is equal to the goal then break out of the while loop
        self.spin(self.left_turn)

def main():
    reachy_controller = Entrance_Movement()
    reachy_controller.run()

if __name__ == "__main__":
    main()
