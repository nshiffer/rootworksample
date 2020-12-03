# Author Nicholas Shiffer
# Github: nshiffer
# Contact: shiffer.7@osu.edu

import create_update_driver as cud
from datetime import datetime

# function determines the action (create or update) that should be taken based on the Command
# @param line_array - a line in the line array
# @param driver_dict - a dictionary that has the driver name as the key and driver object as the value

def determine_action(line_array, driver_dict):
    #Driver command action
    if(line_array[0]=="Driver"):
        #create driver
        driver_dict[line_array[1]] = cud.Driver(line_array[1])
        return

    # Trip command action
    elif(line_array[0]=="Trip"):
        #check if diver in dictionary
        try:
            driver = driver_dict[line_array[1]]
        except:
            print("Error: Driver not registered (" +' '.join(line_array) +") line skipped")
            return

        drive_time = difference_in_hours(line_array[2], line_array[3])

        # in case of error the line will be skipped
        if drive_time == -1:
            print("Error: Invalid time format (" +' '.join(line_array) +") line skipped")
            return


        dist = dist_speed_handler(line_array[4],drive_time)

        if dist == -1:
             print("Error: Invalid distance or speed (" +' '.join(line_array) +") line skipped")
             return

        driver.add_trip(drive_time, dist)

        return
    else:
        print("Error: Command not recognized (" +' '.join(line_array) +") line skipped")
        return

# function that handles input for distances and checks distance and speed for errors
# @param dist: string represention of distance
# @param time: the duration of the trip

def dist_speed_handler(dist, time):
    try:
        ret = float(dist)
    except:
        return -1
    #check for distance error
    if ret <= 0:
        return -1
    #check for speed error
    if ret/time < 5 or ret/time > 100:
        return -1
    return ret

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
