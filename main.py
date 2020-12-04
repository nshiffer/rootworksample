# Author Nicholas Shiffer
# Github: nshiffer
# Contact: shiffer.7@osu.edu

import driver
import input_parsing as inp
import datetime
import sys

# This is the program entry point
# example: ./test_cases/given_test.txt
try:
    in_file = str(sys.argv[1])
except:
    print("Error with command line args")
    answer = input("Would you like to use the defualt test file? (./test_cases/given_test.txt)  \nType Y for yes or any other character to exit: ")
    if answer == "y" or  answer == "Y":
        #"./test_cases/easy_test.txt"
        #"./test_cases/edge_case_max.txt"
        #"./test_cases/edge_case_zeroes.txt"
        in_file = "./test_cases/given_test.txt"
    else:
        sys.exit()
#open, read and close file
with open(in_file) as fp:
    file_lines = fp.readlines()
driver_dict = {}
#parse each line and add to array of objects
for line in file_lines:
    line_array = line.split()
    inp.parse_and_process(line_array, driver_dict)
# print output in expected format
for driver in driver_dict.values():
    driver.prettyPrintInfo()
