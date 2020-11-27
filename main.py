import create_driver
from datetime import datetime

def determine_action(line_array, driver_dict):
    if(line_array[0]=="Driver"):
        driver_dict[line_array[1]] = create_driver.Driver(line_array[1])
        return
    elif(line_array[0]=="Trip"):
        driver = driver_dict[line_array[1]]
        drive_time = difference_in_hours(line_array[2], line_array[3])
        dist = float(line_array[4])
        create_driver.add_trip(driver, drive_time, dist)
        return
    else:
        print("Error: Command not recognized, " +line_array[0])

def difference_in_hours(time1, time2):
    f = "%H:%M"
    return ((datetime.strptime(time2, f) - datetime.strptime(time1, f)).total_seconds())/3600


in_file = "./test_cases/easy_test.txt"
fp = open(in_file)
file_lines = fp.readlines()
out_array = {}
for line in file_lines:
    line_array = line.split()
    determine_action(line_array, out_array)

for driver in out_array:
    out_array[driver].prettyPrintInfo()
