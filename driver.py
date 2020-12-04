# Author Nicholas Shiffer
# Github: nshiffer
# Contact: shiffer.7@osu.edu


class Driver:
    # avg_speed = total_dist / total_time
    # total_dist = sum of all trip distances
    # total_time = sum of all trip times
    def __init__(self, name):
        self.name = name
        self.avg_speed = 0
        self.total_dist = 0
        self.total_time = 0


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

    def update_avg_speed(self, new_dist, new_time):
        #update total speed
        tot_dist = new_dist + self.total_dist
        #Calculate new average speed
        tot_time = new_time + self.total_time
        self.avg_speed = tot_dist/tot_time
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
        self.update_avg_speed(trip_dist, trip_time)
        self.update_distance(trip_dist)
        self.total_time += trip_time
        return
