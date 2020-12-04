# RootWorkSample

Work Sample for Root Insurance, Written in Python

This program will take in a text file of driving information and output each drivers total distance and average speed

Author: Nicholas Shiffer

Github: nshiffer

Contact: shiffer.7@osu.edu

## Running

Make sure you have python 3 >= installed

Install dependencies: pip install -r requirements.txt (or conda install -r requirements.txt, if you use conda) (this is just to make sure you have datetime installed)

To run program: python main.py {test_file_path}

Example: python main.py ./test_cases/given_test.txt

If you do not specify a test file, the default test file will be used.

## Assumptions

-Average speed means total distance divided by total time in hours

-If the difference in time is <=0 then this is an error and should be discarded

-Correct distances are positive, so negative distances should be discarded.

-Backwards travel is recorded as positive distance.

-Second time should be less than first time. If false, will be discarded

## Brainstorming

I knew from the start that I wanted to create a new object that had the average speed and total distance stored. I decided to store this new object in a dictionary for easy access and search when looking up a particular driver. I chose this approach over a data frame or pure dictionary as I wanted to be able to fully customize the object to fit the prompts and my needs. I also wanted to show my ability to create objects that solves a need and can determine the best way to store a given input.

I decided on three files for the implementation, one for input and output, one for initial processing and error handling, and one for object creation and updating. I chose this approach as it is a common approach in python to have one file for the frontend, one for parsing, and one for the backend. While this project does not exactly require frontend and backend structures, I wanted to be able to have the object creation and updating code separate so that it could be used by itself in the future.

## Implementation

There are three main code files main.py, input_parsing.py, and create_driver.py. First, in main.py a file is selected using command line arguments. This file is then parsed in line by line. Each line is split on the white space and turned into an array of strings. In input_parsing.py, the first element in the array is tested to determine what the action should be and the data proceeding is converted to a formatted usable by the driver.py class. Then depending on the action, a function from driver.py is called to handle creating or updating the driver in the dictionary. After successfully completing the action required for each line of input (or discarding the line due to an error), each driver in the dictionary is displayed with their total distance in miles and average speed in mph.


## File Structure

main.py: This opens the file and prints out the given data.

input_parsing.py: This file parses and cleans the input and handles any errors

create_update_driver.py: This file creates and updates drivers in the system.

requirements.txt: package requirements for the program

test_cases: folder that stores test cases for the program. Edge cases test cases are denoted with the prefix "edge_case".

|-- expected_output: folder that contains expected output for the test cases

## Testing

To begin testing, I tested each function and file with input that would be expected as parameters. Once I conformed that was working I moved to unexpected input and output from other functions. I repeated this process until I confirmed that all the connected functions were working with each other.

Testing was then completed using input files and expected output. Testing began with the given sample and expected output. These can be found in test_cases/given_test.txt, and expected_output/expected_output_given_test.txt. From there I moved to random test cases to determine usability and edge case testing to see how the program handles edge cases such as 0 distance, 0 time, and 0 speed, max/very high distance, time and speed.

## Future improvements

-If in the future more statistics were needed to be kept track of, I would use a pandas dataframe to store the data. This would allow for easy calculations and manipulation with a larger data set. I did not use pandas in this work sample as this problem was simple enough to solve be creating a new object which allowed my more control. I also wanted to display my ability to create complete solutions to problems.

-Adding a save file that holds the drivers and driver information from past runs of the program. This file can be loaded back into the program and drivers already in the system can be updated.
