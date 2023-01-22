#!/usr/bin/env python3
import sys
from os.path import exists
from util import get_filepath_to_output_file

# A verification script to verify that all isbns marked "complete" have had files created in the output directory.
# This script takes a single argument (completed_filename) and verifies for each row that the isbn is represented.
# If all are present, it returns a positive message. If not, it lists the missing isbns.
# Example:
#   ./verify_completed.py manga.txt
# The script gets a list of isbns from ../completed/manga.txt. It then uses the input filename and isbn to calculate the
# filenames for the jsons that should have been generated.
def verify_completed():
    input_filepath = get_filepath_to_input_file()
    input_file = open(input_filepath, 'r')
    readline = input_file.readline()
    counter = 0
    failed_files = []
    missing_files = []
    error_array = get_errored_isbns()

    while readline:
        isbn = readline.replace('\n', '')
        filename = get_filepath_to_output_file(isbn)

        if not exists(filename):
            if isbn in error_array:
                failed_files.append(filename)
            else:
                missing_files.append(filename)

        counter+=1
        readline = input_file.readline()

    if len(missing_files) > 0:
        print('Failed to find the following files:\n')
        for file in missing_files:
            print(file + '\n')
    else:
        print('All {0} files are present!'.format(counter))

    if len(failed_files) > 0:
        print('Skipped the following files, as these are present in the error directory:\n')
        for file in failed_files:
            print(file + '\n')

    input_file.close()


def get_errored_isbns():
    error_file_path = "../errors/%s" % sys.argv[1]
    error_file = open(error_file_path, 'r')
    readline = error_file.readline()
    error_array = []

    while readline:
        isbn = readline.replace('\n', '')
        error_array.append(isbn)

        readline = error_file.readline()
    return error_array


# Based on the input provided in the first (and only) argument, return the file path to the input file including the filename.
def get_filepath_to_input_file():
    return "../completed/%s" % sys.argv[1]


if __name__ == "__main__":
    verify_completed()
