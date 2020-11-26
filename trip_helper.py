def update_avg_speed(driver, speed):
  driver.avgSpeed = (speed+(driver.avgSeed*len(driver.trips))/(len(driver.trips)+1)
  return
  
def update_distance(driver, new_distance):
  driver.distance = driver.distance + new_distance
  return
  
def add_trip(driver, trip_time, trip_length):
  update_avg_speed(driver, (trip_length/trip_time))
  update_distance(driver, trip_length)
  
  
