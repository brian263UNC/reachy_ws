from mobile_base_sdk import MobileBaseSDK


class Entrance_Movement:
    def __init__(self):
        self.mobile_base = MobileBaseSDK('10.42.0.1') # Make sure to update the IP address yours TODO
        self.arrived_at_goal = False # boolean check if Reachy has arrived at the set goal
        self.final_distance = 5.0 # distance to travel in meters

    def reset_coordinates(self):
        self.mobile_base.reset_odometry()

    def accelerate(self):
        # TODO
        pass

    # Reset's the coordinate system and then spins Reachy by the desired degree amount
    def spin(self, degree):
        self.reset_coordinates()
        self.mobile_base.goto(x=0.0, y=0.0, theta=degree)

    def total_distance_traveled(self, x, y, theta):
        # TODO
        pass

    def run(self):
        travel_distance = 0.0
        while(True):
            total_revolutions = 5
            for i in range(total_revolutions):
                self.mobile_base.goto(x=0.1, y=0.1, theta=0)
                print("Current Iteration: " + i)
            self.reset_coordinates()
            travel_distance += 0.5
            print("Total distance traveled: " + travel_distance)
            if travel_distance == self.final_distance: break # real ugly, but gets the job done, if the distance traveled is equal to the goal then break out of the while loop
        self.spin(90)

def main():
    reachy_controller = Entrance_Movement()
    reachy_controller.run()

if __name__ == "__main__":
    main()
