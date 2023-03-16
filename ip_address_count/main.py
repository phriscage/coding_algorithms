#!/usr/bin/env python
# use the environment python for this example. I would recommend adding this
# as a service or function with the runtime and executable libraries are
# consistant and remove dependencies
import os.path
from collections import defaultdict

def parse_file(file_name):
    """ iterate through the file and collect the total number of IP address
        args:
            file_name (string): the input file name string
        Returns:
            top_ips (dict): dictionary of key (ip) and total occurances
    """
    if not os.path.isfile(file_name):
        raise TypeError("Bad file: '%s'" % file_name)
    top_ips = defaultdict(int)
    with open(file_name) as file_buffer:
        for line in file_buffer:
            ip = line.split()[-1]
            top_ips[ip] += 1
    return top_ips

def get_values_by_total(values, limit=10, reverse=True):
    """ sort the values by a count """
    return sorted(values.iteritems(), key=lambda x: x[1],
            reverse=reverse)[:limit]

def get_values_by_ip(values, limit=10, reverse=True):
    """ sort the values by a ip and count """
    new_values = defaultdict(list)
    for ip, count in values.iteritems():
        new_values[count].append(ip)
        if len(new_values) >= limit:
            break
    return sorted(new_values.iteritems(), reverse=reverse)[:limit]


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        raise TypeError("Not enough files")
    try:
        top_ips = parse_file(sys.argv[1])
    except Exception as error:
        print("Try again!")
        raise error
    print("values by total occurances")
    for idx, ip in enumerate(get_values_by_total(top_ips), 1):
        print(idx, ip)
    print("values by total and ips occurances")
    for idx, ip in enumerate(get_values_by_ip(top_ips), 1):
        print(idx, ip)
