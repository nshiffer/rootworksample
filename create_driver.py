class Driver:
    def __init__(self, name):
        self.name = name
        self.avgSpeed = 0
        self.totalDist = 0
        self.pastTrips = []

    def prettyPrintInfo(self):
        if self.totalDist > 1:
            distString = str(self.totalDist)+" miles"
        elif self.totalDist == 1:
            distString = str(self.totalDist)+" mile"
        else:
            #Distance is zero so only print distance
            print(self.name+": "+str(self.totalDist)+" miles")
            return
        print(self.name+": "+distString+" @ "+str(self.avgSpeed)+" mph")
        return

def update_avg_speed(driver, speed):
    driver.avgSpeed = (speed+(driver.avgSpeed*len(driver.pastTrips))/(len(driver.pastTrips)+1))
    return

def update_distance(driver, new_distance):
    driver.totalDist = driver.totalDist + new_distance
    return

def add_trip(driver, trip_time, trip_length):
    driver.pastTrips.append((trip_time, trip_length))
    update_avg_speed(driver, (trip_length/trip_time))
    update_distance(driver, trip_length)
