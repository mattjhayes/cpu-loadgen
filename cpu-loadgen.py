#!/usr/bin/python

#*** Import sys and getopt for command line argument parsing:
import sys, getopt

import time

def main(argv):
    """
    Main function of cpu-loadgen
    Use this program to create maximum CPU load
    as a factor for other tests.
    """
    version = "0.1.0"
    start_delay = 0
    test_duration = 60
    finished = 0
    base_number = 1234345081790745098098234

    #*** Start by parsing command line parameters:
    try:
        opts, args = getopt.getopt(argv, "hs:t:v",
                                ["help",
                                "start-delay=",
                                "test-duration=",
                                "version"])
    except getopt.GetoptError as err:
        print "cpu-loadgen: Error with options:", err
        print_help()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-s", "--start-delay"):
            start_delay = arg
        elif opt in ("-t", "--test-duration"):
            test_duration = arg
        elif opt in ("-h", "--help"):
            print_help()
            sys.exit()
        elif opt in ("-v", "--version"):
            print 'hort.py version', version
            sys.exit()

    #*** Convert times to floats:
    start_delay = float(start_delay)
    test_duration = float(test_duration)

    print "sleeping for", start_delay, "seconds"
    time.sleep(start_delay)

    start_time = time.time()

    print "starting cpu load"
    while not finished:
        result = base_number * base_number
        result = base_number * base_number
        result = base_number * base_number
        result = base_number * base_number
        current_time = time.time()
        if current_time > (start_time + test_duration):
            finished = 1

    print "test finished"
    return 1

def print_help():
    """
    Print out the help instructions
    """
    print """
CPU Load Generator
---------------------------------

Use this program to create CPU load, as a factor for other tests.
Creates a maximum (close to 100%) CPU load while running.

Usage:
  python cpu-loadgen.py [options]

Example usage:
  python cpu-loadgen.py --start-delay 10 --test-duration 60

Options:
 -h  --help            Display this help and exit
 -s  --start-delay     Time to delay start for (default 0 seconds)
 -t  --test-duration   How long to run the test for (default 60 seconds)
 -v, --version         Output version information and exit
 """
    return()

if __name__ == "__main__":
    #*** Run the main function with command line
    #***  arguments from position 1
    main(sys.argv[1:])
