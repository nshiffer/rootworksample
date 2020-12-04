# Author Nicholas Shiffer
# Github: nshiffer
# Contact: shiffer.7@osu.edu

import driver as driv
from datetime import datetime

# function determines the action (create or update) that should be taken based on the Command
# @param line_array - a line in the line array
# @param driver_dict - a dictionary that has the driver name as the key and driver object as the value

def parse_and_process(line_array, driver_dict):
    #Driver command action
    if(line_array[0]=="Driver"):
        #create driver
        driver_dict[line_array[1]] = driv.Driver(line_array[1])
        return

    # Trip command action
    elif(line_array[0]=="Trip"):
        #check if diver in dictionary
        #this is using if else as that is the standard way to check a dictionary, try except is used when that is the default handeler
        if line_array[1] in driver_dict:
            driver = driver_dict[line_array[1]]
        else:
            print("Error: Driver not registered (" +' '.join(line_array) +") line skipped")
            return

        drive_time = difference_in_hours(line_array[2], line_array[3])

        # in case of error the line will be skipped
        if drive_time == -1:
            print("Error: Invalid time format (" +' '.join(line_array) +") line skipped")
            return


        dist = dist_to_float(line_array[4])

        if dist == -1:
             print("Error: Invalid distance or speed (" +' '.join(line_array) +") line skipped")
             return

        speed_check = check_speed(dist, drive_time)

        if speed_check == -1:
             print("Error: Invalid distance or speed (" +' '.join(line_array) +") line skipped")
             return

        driver.add_trip(drive_time, dist)

        return
    else:
        print("Error: Command not recognized (" +' '.join(line_array) +") line skipped")
        return

# function that handles input for distances and checks distance for errors
# @param dist: string represention of distance
# @param time: the duration of the trip

def dist_to_float(dist):
    try:
        ret = float(dist)
    except:
        return -1
    #check for distance error
    if ret <= 0:
        return -1
    return ret

# function that checks the speed is greater than 5 and less than 100
# @param dist: string represention of distance
# @param time: the duration of the trip

def check_speed(dist, time):
    if dist/time < 5 or dist/time > 100:
        return -1
    else:
        return 1


# function that determines the difference of two times and outbuts them as a difference in difference
# @param time1 - the earlier time in the format hours:minutes
# @param times - the later time in the format hours:minutes

def difference_in_hours(time1, time2):
    format = '%H:%M'
    try:
        ret = ((datetime.strptime(time2, format) - datetime.strptime(time1, format)).total_seconds())/3600
    except ValueError:
        return -1
    #check for time less than 0 error
    if ret <= 0:
        return -1
    return ret
