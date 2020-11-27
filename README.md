# RootWorkSample

Work Sample for Root Insurance, Written in Python

Author: Nicholas Shiffer

Github: nshiffer

## Assumptions

If the difference in time is <=0 then this is an error and should be discarded
Correct distances are positive, so negative distances should be discarded.
Backwards travel is considered positive distance.
Second time should be less than first time. If true, will be discarded

## Brainstorming

I knew from the start that I would wanted to create a new object that had the average speed and total distance stored. I decided to store this new object in a dictionary for easy access and search when looking up a particular driver.

## Implementation

There are two main code files main.py and create_driver.py. First, in main.py a file is selected using command line arguments. This file is then parsed in line by line. Each line is split on the white space and turned into an array of strings. The first element in the array is tested to determine what the action should be. Then depending on the action, a function from create_driver.py is called to handle creating or updating the driver in the dictionary. After successfully completing the action required for each line of input (or discarding the line due to an error), each driver in the dictionary is displayed with their total distance in miles and average speed in mph.


## File Structure

main: This file contains code that opens the file, parses, cleans and prints out the given data.

create_driver: this file contains code that creates and updates drivers in the system.

test_cases: folder that stores test cases for the program. Edge cases test cases are denoted with the prefix "edge_case".

Expected_output: folder that contains expected output for the test cases

## Future improvements

- If in the future more statistics were needed to be kept track of, I would use a pandas dataframe to store the data. This would allow for easy calculations and manipulation with a larger data set. I did not use pandas in this work sample as this problem was simple enough to solve be creating a new object which allowed my more control. I also wanted to display my ability to create complete solutions to problems.

- Adding a save file that holds the drivers and driver information from past runs of the program. This file can be loaded back into the program and drivers already in the system can be updated.
