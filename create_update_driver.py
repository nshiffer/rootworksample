# Author Nicholas Shiffer
# Github: nshiffer
# Contact: shiffer.7@osu.edu

class Driver:
    def __init__(self, name):
        self.name = name
        self.avg_speed = 0
        self.totalDist = 0
        self.pastTrips = []

    def prettyPrintInfo(self):
        # determine if mile should be singular or plural
        if self.totalDist > 1:
            distString = "{:.0f}".format(self.totalDist)+" miles"
        elif self.totalDist == 1:
            distString = "{:.0f}".format(self.totalDist)+" mile"
        else:
            #Distance is zero so only print distance
            print(self.name+": "+str(self.totalDist)+" miles")
            return

        # print to the terminal
        print(self.name+": "+distString+" @ "+"{:.0f}".format(self.avg_speed)+" mph")
        return

    def update_avg_speed(self, speed):
        total = speed + self.avg_speed*len(self.pastTrips)
        new_avg = total / (len(self.pastTrips)+1.0)
        self.avg_speed = new_avg
        return

    def update_distance(self, new_distance):
        self.totalDist = self.totalDist + new_distance
        return

    def add_trip(self, trip_time, trip_dist):
        self.update_avg_speed((trip_dist/trip_time))
        self.update_distance(trip_dist)
        self.pastTrips.append((trip_time, trip_dist))
        return
