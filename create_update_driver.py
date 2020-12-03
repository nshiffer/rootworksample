# Author Nicholas Shiffer
# Github: nshiffer
# Contact: shiffer.7@osu.edu

class Driver:
    def __init__(self, name):
        self.name = name
        self.avg_speed = 0
        self.total_dist = 0
        self.past_trips = []


    # function that prints output in the desired format

    def prettyPrintInfo(self):
        # determine if mile should be singular or plural
        if self.total_dist > 1:
            dist_string = "{:.0f}".format(self.total_dist)+" miles"
        elif self.total_dist == 1:
            dist_string = "{:.0f}".format(self.total_dist)+" mile"
        else:
            #Distance is zero so only print distance
            print(self.name+": "+str(self.total_dist)+" miles")
            return

        # print to the terminal
        print(self.name+": "+dist_string+" @ "+"{:.0f}".format(self.avg_speed)+" mph")
        return

    # function updates average speed in the object
    # @param speed - the speed in mph to be added

    def update_avg_speed(self, speed):
        total = speed + self.avg_speed*len(self.past_trips)
        new_avg = total / (len(self.past_trips)+1.0)
        self.avg_speed = new_avg
        return

    # function updates the total distance
    # @param new_distance: the distance to be added

    def update_distance(self, new_distance):
        self.total_dist = self.total_dist + new_distance
        return

    # function that adds a new trip to the object
    # @param trip_time: the time duration of the trip
    # @param trip_dist: the distance of the trip

    def add_trip(self, trip_time, trip_dist):
        self.update_avg_speed((trip_dist/trip_time))
        self.update_distance(trip_dist)
        self.past_trips.append((trip_time, trip_dist))
        return
