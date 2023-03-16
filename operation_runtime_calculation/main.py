#!/usr/bin/env python
# assuming whoever is running this is leveraging at least python 2.x.
# I will try to make compatible to python 3 too
"""
	This logic will iterate over a file and capture the start/end times for specific operations
"""
import os.path
import datetime

def _validate_file(file_name):
    """ validate the file is readable and not too big in size """
    if not os.path.isfile(file_name):
        raise TypeError("Bad file: '%s'" % file_name)
    pass

def _validate_line(line):
    """ validate the line has the correct number values """
    pass

def _get_runtime(end_time, start_time):
    """ get the runtime in seconds from two iso 8601 timestamp strings """
    end_time = datetime.datetime.strptime(end_time, '%Y-%m-%dT%H:%M')
    start_time = datetime.datetime.strptime(start_time, '%Y-%m-%dT%H:%M')
    return (end_time - start_time).seconds

def parse_file(file_name):
    """ parse the file line by line and calculate the difference in time """
    _validate_file(file_name)
    operations = dict()
    runtimes = dict()
    with open(file_name) as file_buffer:
        for line in file_buffer:
            print(line.split())
            time_stamp, _, name, start_end = line.split()
            if not operations.get(name, None):
                if start_end == 'Start':
                    operations[name] = time_stamp
                else:
                    raise ValueError("End exists before Start")
                continue
	    ## end time - start time = runtime
            runtime = _get_runtime(time_stamp,operations.get(name))
            runtimes[name] = runtime
    return runtimes

def calculate_average(data):
    """ calculate the average values for the dictionary """
    print(data.values())
    return sum(data.values()) / len(data.values())


def main(**args):
    """ run the main logic """
    print(calculate_average(parse_file(args['file_name'])))

if __name__ == '__main__':
    import sys
    main(file_name=sys.argv[1])
